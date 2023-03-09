import aws_cdk as core
import aws_cdk.assertions as assertions

from python_aws_cdk_101.python_aws_cdk_101_stack import PythonAwsCdk101Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in python_aws_cdk_101/python_aws_cdk_101_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PythonAwsCdk101Stack(app, "python-aws-cdk-101")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
