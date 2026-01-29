pipeline {
  agent any

  stages {

    stage('Checkout Code') {
      steps {
        git branch: 'main', url: 'https://github.com/Pragatitrip/DevSecOps-Flask.git'
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
            -Dsonar.host.url=http://host.docker.internal:9000 \
            -Dsonar.login=$SONAR_TOKEN
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t devsecops-flask-app ./app'
      }
    }

    stage('Trivy Image Scan') {
      steps {
        sh 'trivy image devsecops-flask-app'
      }
    }
  }
}
