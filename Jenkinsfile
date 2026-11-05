
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\hp\\AppData\\Local\\Python\\bin\\python.exe'
    }

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

                bat '''
                    "%PYTHON%" --version
                    "%PYTHON%" -m venv venv
                    venv\\Scripts\\python.exe -m pip install --upgrade pip
                    venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running automated tests'

                bat '''
                    venv\\Scripts\\python.exe -m pytest tests/ -v
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
