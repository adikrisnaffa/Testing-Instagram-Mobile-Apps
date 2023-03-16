pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'pip install Appium-Python-Client'
                sh 'pip install pytest'
            }
        }
        stage('Run tests') {
            steps {
                sh 'pytest instagram.py -m test_instagram --junitxml=test-results.xml'
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
    }
}
z
