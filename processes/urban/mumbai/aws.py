# processes/urban/mumbai/aws.py

def process_aws(data):

    aws = data.get(
        "aws_locations",
        []
    )

    return {

        "status": "ACTIVE",

        "message":

        f"{len(aws)} Automatic Weather "

        f"Stations operational."

    }