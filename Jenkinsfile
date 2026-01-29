pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pragatitrip/DevSecOps-Flask.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-flask:latest .'
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                trivy image --severity HIGH,CRITICAL devsecops-flask:latest || true
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished'
        }
    }
}
