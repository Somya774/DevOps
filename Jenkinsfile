pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean package'  // Adjust based on your build tool
            }
        }
        
        stage('Test') {
            steps {
                sh 'mvn test'  // Run tests
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add deployment script here (Docker, Kubernetes, etc.)
            }
        }
    }
}
