def call(Map config = [:]) {
    pipeline {
        agent any

        options {
            timestamps()
            buildDiscarder(logRotator(numToKeepStr: '20'))
            disableConcurrentBuilds()
        }

        environment {
            APP_NAME = "${config.appName ?: 'unknown-app'}"
            LANGUAGE = "${config.language ?: 'generic'}"
        }

        stages {
            stage('Checkout') {
                steps {
                    checkout scm
                }
            }

            stage('Static Checks') {
                when { expression { return config.runStaticChecks == true } }
                steps {
                    echo "Running static checks for ${APP_NAME}"
                    echo 'Example: lint, formatting and policy checks would run here.'
                }
            }

            stage('Unit Tests') {
                when { expression { return config.runUnitTests == true } }
                steps {
                    echo "Running unit tests for ${APP_NAME}"
                    echo 'Example: pytest, junit, npm test or equivalent test command.'
                }
            }

            stage('Build Artifact') {
                steps {
                    echo "Building artifact for ${APP_NAME}"
                    echo 'Example: package, container build or artifact publishing.'
                }
            }

            stage('Security Scan') {
                when { expression { return config.runSecurityScan == true } }
                steps {
                    echo 'Running security scan placeholder.'
                    echo 'Example: dependency scan, SAST, container scan or SD Elements workflow.'
                }
            }

            stage('Deployment Approval') {
                when { expression { return config.requireDeploymentApproval == true } }
                steps {
                    input message: "Approve deployment for ${APP_NAME}?", ok: 'Approve'
                }
            }

            stage('Publish Metrics') {
                steps {
                    echo 'Publishing delivery metrics: lead time, deployment frequency and build result.'
                }
            }
        }

        post {
            always {
                echo "Pipeline finished for ${APP_NAME} with status: ${currentBuild.currentResult}"
            }
        }
    }
}
