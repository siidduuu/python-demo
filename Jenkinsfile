pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo "Checking out source..."
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Complete') {
            steps {
                echo "Python build completed successfully."
            }
        }
    }
}
