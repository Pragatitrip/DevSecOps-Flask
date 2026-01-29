pipeline {
  agent any

  environment {
    SONAR_HOST_URL = "http://sonarqube:9000"
    IMAGE_NAME = "devsecops-flask-app"
  }

  stages {

    stage('Checkout Code') {
      steps {
        git 'https://github.com/Pragatitrip/DevSecOps-Flask.git'
      }
    }

    stage('SonarQube Analysis') {
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
            -Dsonar.host.url=http://sonarqube:9000 \
            -Dsonar.login=$SONAR_TOKEN
        '''
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t devsecops-flask-app ./app'
      }
    }

    stage('Trivy Scan') {
      steps {
        sh 'trivy image devsecops-flask-app'
      }
    }
  }
}
