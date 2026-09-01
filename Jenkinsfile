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
            sh '''
                docker compose logs --tail=100
            '''
        }
    }
}