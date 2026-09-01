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
                    docker compose run --rm api pytest
                '''
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