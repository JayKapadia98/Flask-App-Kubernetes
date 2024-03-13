import boto3

def create_ecr(repositoryName):

    ecr_cli = boto3.client('ecr')

    try:
        response = ecr_cli.create_repository(repositoryName=repositoryName)
        print("ECR Repository created successfully!")
        print("Repo URI: ",response['repository']['repositoryUri'])
    except ecr_cli.exceptions.RepositoryAlreadyExistsException:
        print("Repo Already Exists")
    except Exception as e:
        print("An error as follows", str(e))

        
repositoryName = "jkpedia-repo"
create_ecr(repositoryName)



