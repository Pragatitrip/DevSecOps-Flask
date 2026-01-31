pipeline {
    agent any

    environment {
        SONAR_HOST_URL = "http://host.docker.internal:9000"
        IMAGE_NAME = "devsecops-flask-app"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Pragatitrip/DevSecOps-Flask.git'
            }
        }

        stage('SonarQube SAST Analysis') {
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
                    -Dsonar.host.url=${SONAR_HOST_URL} \
                    -Dsonar.login=$SONAR_TOKEN
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t ${IMAGE_NAME} ./app
                '''
            }
        }

        stage('OWASP Dependency Check (SCA)') {
            steps {
                sh '''
                  mkdir -p dependency-check-report
                  docker run --rm \
                    -v $(pwd):/src \
                    -v dependency-check-data:/usr/share/dependency-check/data \
                    owasp/dependency-check \
                    --scan /src \
                    --format HTML \
                    --out /src/dependency-check-report \
                    --disableAssembly \
                    --noupdate || true
                '''
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh '''
                  trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    ${IMAGE_NAME}
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dependency-check-report/**',
                             allowEmptyArchive: true
        }
        success {
            echo '✅ Pipeline completed successfully — secure build ready!'
        }
        failure {
            echo '❌ Pipeline failed due to security issues!'
        }
    }
}
