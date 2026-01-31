pipeline {
    agent any

    environment {
        IMAGE_NAME = "devsecops-flask-app"
        SONAR_HOST_URL = "http://host.docker.internal:9000"
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

        stage('SonarQube Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
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
                  rm -rf owasp-report
                  mkdir -p owasp-report

                  docker run --rm \
                    -u root \
                    -v $(pwd):/src \
                    -v dependency-check-data:/usr/share/dependency-check/data \
                    owasp/dependency-check \
                    --scan /src \
                    --format HTML \
                    --out /src/owasp-report \
                    --project "DevSecOps Flask App" \
                    --disableAssembly \
                    --noupdate
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
            archiveArtifacts artifacts: 'owasp-report/**',
                             allowEmptyArchive: true
        }
        success {
            echo '✅ Pipeline completed successfully — secure build ready!'
        }
        failure {
            echo '❌ Pipeline failed due to Quality Gate or security issues!'
        }
    }
}
