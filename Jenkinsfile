pipeline{
        agent any
        environment{
            DATABASE_URI= credentials("DATABASE_URI")
            DOCKER_ID=credentials("DockerID")
        }
        stages{
            stage('Setup'){
                steps{
                    sh "bash scripts/setup.sh"
                }
            }
            stage('Test'){
                steps{
                    sh "bash scripts/test.sh"
                }
            }
            stage('Build'){
                steps{
                    sh "bash scripts/build.sh"
                }
            }
            stage('Config'){
                steps{
                    sh "bash scripts/config.sh"
                }
            }
            stage('Deploy'){
                steps{
                    sh "bash scripts/deploy.sh"
                }
            }
        }
}