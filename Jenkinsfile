pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        REQUIREMENTS = 'requirements.txt'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm  // Pulls the latest code from the repository
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                script {
                    if (!fileExists(VENV_DIR)) {
                        sh 'python3 -m venv venv'  // Create virtual environment
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install distutils (needed for Python 3.12)
                    sh 'sudo apt-get install python3-distutils -y'  // Install distutils package

                    // Upgrade setuptools to ensure the environment is up-to-date
                    sh '. venv/bin/activate && pip install --upgrade setuptools'  // Upgrade setuptools

                    // Install other dependencies from the requirements.txt
                    sh '. venv/bin/activate && pip install -r ${REQUIREMENTS}'  // Install dependencies
                }
            }
        }

        stage('Run Dependency Check') {
            steps {
                script {
                    sh 'pip install owasp-dependency-check'  // Install Dependency-Check
                    sh 'dependency-check --project "Python App" --scan . --out ./dependency-check-report'  // Run scan
                }
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportName: 'Dependency Check Report',
                    reportDir: './dependency-check-report',
                    reportFiles: 'dependency-check-report.html'  // Publish the scan report
                ])
            }
        }

        stage('Clean Up') {
            steps {
                sh 'rm -rf venv'  // Optionally remove the virtual environment
            }
        }
    }

    post {
        always {
            echo 'Success'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
