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
                sh 'docker build -t devsecops-flask-app .'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'trivy image devsecops-flask-app || true'
            }
        }
    }
}

