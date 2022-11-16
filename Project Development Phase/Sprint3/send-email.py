# def predict(filename):

#         channel = ClarifaiChannel.get_grpc_channel()
#         stub = service_pb2_grpc.V2Stub(channel)

#         metadata = (('authorization', 'Key ' + C_PAT),)

#         userDataObject = resources_pb2.UserAppIDSet(user_id=C_USER_ID, app_id=C_APP_ID)

#         post_model_outputs_response = stub.PostModelOutputs(
#             service_pb2.PostModelOutputsRequest(
#                 user_app_id=userDataObject,
#                 model_id=C_MODEL_ID,
#                 # version_id={MODEL_VERSION},  # This is optional. Defaults to the latest model version.
#                 inputs=[
#                     resources_pb2.Input(
#                         data=resources_pb2.Data(
#                             image=resources_pb2.Image(
#                                 url=filename
#                             )
#                         )
#                     )
#                 ]
#             ),
#             metadata=metadata
#         )

#         if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
#             print(post_model_outputs_response.status)
#             raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

#         # Since we have one input, one output will exist here.
#         output = post_model_outputs_response.outputs[0]

#         flash("Predicted concepts:")
#         for concept in output.data.concepts:
#             flash("%s   %.2f" % (concept.name, concept.value))

#         # Uncomment this line to print the full Response JSON
#         #print(post_model_outputs_response)
