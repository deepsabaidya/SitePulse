
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out SitePulse source code'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo 'Setting up Python environment'

                sh '''
                    python3 --version
                    python3 -m venv venv
                    venv/bin/pip install --upgrade pip
                    venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests'

                sh '''
                    venv/bin/python -m pytest tests/ -v
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'SitePulse build completed successfully'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: SitePulse pipeline completed!'
        }

        failure {
            echo 'FAILURE: Check the pipeline logs.'
        }

        always {
            echo 'Pipeline execution finished.'
        }
    }
}
