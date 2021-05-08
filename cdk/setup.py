import setuptools


with open("README.md") as fp:
    long_description = fp.read()


cdk_version='1.102.0'

setuptools.setup(
    name="cdk",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "cdk"},
    packages=setuptools.find_packages(where="cdk"),

    install_requires=[
        f"aws-cdk.core=={cdk_version}",
        f"aws-cdk.aws_kinesis=={cdk_version}",
        f"aws-cdk.aws_dynamodb=={cdk_version}",
        f"aws_cdk.aws_ec2=={cdk_version}",
        f"aws_cdk.aws_apigateway=={cdk_version}",
        f"aws_cdk.aws_iam=={cdk_version}",
        f"aws_cdk.aws_codedeploy=={cdk_version}",
        f"aws_cdk.aws_codecommit=={cdk_version}",
        f"aws_cdk.aws_codepipeline=={cdk_version}",
        f"aws_cdk.pipelines=={cdk_version}",
        f"aws_cdk.aws_codepipeline_actions=={cdk_version}",
        f"aws_cdk.aws_lambda=={cdk_version}",
        f"aws_cdk.aws_logs=={cdk_version}",
        f"aws_cdk.aws_lambda_event_sources=={cdk_version}",
        "requests",
        "pytest==6.0.1"
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
