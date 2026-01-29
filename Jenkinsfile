pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsecops-flask-app"
        SONAR_HOST_URL = "http://localhost:9000"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pragatitrip/DevSecOps-Flask.git'
            }
        }

        stage('SonarQube Analysis (SAST)') {
            environment {
                SONAR_TOKEN = credentials('sonar-token')
            }
            steps {
                sh '''
                docker run --rm \
                  -v $(pwd):/usr/src \
                  sonarsource/sonar-scanner-cli \
                  -Dsonar.projectKey=devsecops-flask \
                  -Dsonar.sources=. \
                  -Dsonar.host.url=http://localhost:9000 \
                  -Dsonar.login=$SONAR_TOKEN
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-flask-app .'
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh 'trivy image devsecops-flask-app'
            }
        }
    }
}
