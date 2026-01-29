pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devsecops-flask-app .'
            }
        }

        stage('Trivy Security Scan') {
            steps {
                sh 'trivy image devsecops-flask-app'
            }
        }
    }
}

