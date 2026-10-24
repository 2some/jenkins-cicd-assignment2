pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 --version'
                sh 'python3 -m pip --version'
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 -m py_compile app.py
                    echo "Build validation successful"
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest -v'
            }
        }

        stage('Package Artifact') {
            steps {
                sh '''
                    mkdir -p dist
                    tar --exclude='.git' \
                        --exclude='_pycache_' \
                        --exclude='dist' \
                        -czf dist/python-app.tar.gz \
                        app.py README.md
                '''
                archiveArtifacts artifacts: 'dist/python-app.tar.gz',
                                 fingerprint: true
            }
        }
    }
}