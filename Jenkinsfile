pipeline{
	agent any
	stages{
	    stage('Instalación'){
		    steps{
			    sh "ansible-playbook -i  ./jenkins ./Pipeline.yml"
			}
		}
		stage('Verificación de código'){
			environment{
				AWS_ACCESS_KEY_ID='AKIAJAI5GCXWYCRHPAUQ'
				AWS_SECRET_ACCESS_KEY='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'
			}
			steps{
				//sh ". /home/ubuntu/SCATUAZ/env_scatuaz/bin/activate"
				sh "autopep8 -i *.py */*.py"
				sh "flake8 --exclude = *migrations*,*settings*"
			}
		}
		stage('Testing'){
			steps{
				sh "python manage.py test Trabajaor"
				sh "behave  features/*.feature"
				sh "coverage run --source = '.' --omit = *test*, *migrations*, *__init* manage.py"
				sh "coverage report"
				sh "coverage html"
			}
		}
		stage('Build'){
			steps{
				echo "Build"
			}
		}
		stage('Servidor de pre-producción'){
		      steps{
				sh "ansible-playbook -i ./ pre_aws_ec2.yml ./ Pipeline.yml"	
		      }
		}
		stage('Servidor de producción'){
			input{
			        message "Quieres hacer el despligue a producción?"
			        ok "Si"
			}
			steps{
				echo "ansible-playbook -i ./ Pipeline.yml"
			}
		}
	}
}
chuckNorris()
