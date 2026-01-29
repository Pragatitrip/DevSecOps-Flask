pipeline {
    agent any

    stage('Build Docker Image') {
    steps {
        sh 'docker build -t devsecops-flask-app ./app'
    }
}

        stage('Trivy Security Scan') {
            steps {
                sh 'trivy image devsecops-flask-app'
            }
        }
    }
}

