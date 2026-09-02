pipeline {

    agent {
        label 'python-agent'
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }


        stage('Verify Docker') {
            steps {
                sh '''
                    echo $DOCKER_HOST
                    docker --version
                    docker compose version
                    docker ps
                '''
            }
        }


        stage('Create Environment') {
            steps {

                echo 'Creating .env from Jenkins credentials...'

                withCredentials([
                    string(
                        credentialsId: 'banking-db-password',
                        variable: 'DB_PASSWORD'
                    ),
                    string(
                        credentialsId: 'groq-api-key',
                        variable: 'GROQ_API_KEY'
                    )
                ]) {

                    sh '''
                        cat > .env <<EOF
DB_HOST=mysql
DB_PORT=3306
DB_USER=root
DB_PASSWORD=$DB_PASSWORD
DB_NAME=banking_db

REDIS_HOST=redis
REDIS_PORT=6379

GROQ_API_KEY=$GROQ_API_KEY
EOF
                    '''
                }
            }
        }


        stage('Build') {
            steps {
                echo 'Building Docker images...'

                sh '''
                    docker compose build
                '''
            }
        }


        stage('Start Dependencies') {
            steps {
                echo 'Starting MySQL and Redis...'

                sh '''
                    docker compose up -d mysql redis
                '''
            }
        }


      stage('Run Tests') {
    steps {
        echo 'Running tests...'

        sh '''
            docker compose run --rm api sh -c "
                echo 'Current directory:'
                pwd

                echo 'Files:'
                ls -la

                echo 'Python version:'
                python --version

                echo 'Pytest version:'
                python -m pytest --version

                echo 'Running pytest:'
                python -m pytest -vv -s
            "
        '''
    }
}

stage('Push Docker Image') {
    steps {

        echo 'Pushing Docker image to Docker Hub...'

        withCredentials([
            usernamePassword(
                credentialsId: 'dockerhub-credentials',
                usernameVariable: 'DOCKERHUB_USERNAME',
                passwordVariable: 'DOCKERHUB_TOKEN'
            )
        ]) {

            sh '''
                echo "$DOCKERHUB_TOKEN" | docker login \
                    -u "$DOCKERHUB_USERNAME" \
                    --password-stdin

                docker tag banking_risk_investigation-api:latest \
                    $DOCKERHUB_USERNAME/banking-risk-investigation:latest

                docker push \
                    $DOCKERHUB_USERNAME/banking-risk-investigation:latest
            '''
        }
    }
}

stage('Deploy to EC2') {
    steps {
        echo 'Deploying latest image to EC2...'

        sshagent(credentials: ['ec2-ssh-key']) {
            sh '''
                ssh -o StrictHostKeyChecking=no ubuntu@13.61.100.176 "
                    cd ~/banking-risk &&
                    docker compose pull &&
                    docker compose up -d &&
                    docker compose ps
                "
            '''
        }
    }
}
    }


    post {

        success {
            echo 'CI pipeline completed successfully.'
        }

        failure {
            echo 'CI pipeline failed.'
        }

        always {
            sh '''
                rm -f .env
            '''
        }
    }
}