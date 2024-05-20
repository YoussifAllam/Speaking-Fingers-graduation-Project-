from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AudioFileSerializer ,AudioFile_upload_Serializer
from .tasks import speech_to_text, text_to_phonetic
from .detailed_similarity_analysis import detailed_similarity_analysis_and_feedback
from rest_framework import status
from .models import Audio_Model

def get_current_host(request):
    protocol = request.is_secure() and 'https' or 'http'
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


class SpeechAnalysisView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AudioFile_upload_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("______________________________Serializer Data:", serializer.data) 
            # if 'reference_text' not in request.data or 'audio_file' not in request.data : 
            #     return Response ({'message' : 'you should enter audio_file and reference_text' } , status=status.HTTP_400_BAD_REQUEST)
            audio_file = Audio_Model.objects.get(id=serializer.data['id'])
            reference_text = request.data.get('reference_text')
            
            host  = get_current_host(request)
            audio_path = f'media/{audio_file.Audio}'
            print(audio_path,  '=====================')
            text_output = speech_to_text(audio_path)

            speech_text_text_to_phonetic = text_to_phonetic(text_output)

            refrence_text_phonetic = text_to_phonetic(reference_text)

            similarity, errors, feedback = detailed_similarity_analysis_and_feedback(refrence_text_phonetic, speech_text_text_to_phonetic)

            return Response({
                'status' : 'success' , 
                'data' :
                  {
                "text_output": text_output,
                "phonetic_output": speech_text_text_to_phonetic,
                "similarity_score": similarity,
                "errors": errors,
                "feedback": feedback
                }
            } , status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




# speech_text = speech_to_text('/content/clay.mp3') # take audio path
# speech_text_text_to_phonetic = text_to_phonetic(speech_text)
# print(speech_text_text_to_phonetic)


# refrence_text = input('Enter a text : ') # take text from user
# refrence_text_phonetic = text_to_phonetic(refrence_text)
# print(refrence_text_phonetic)



# # Assuming refrence_text_phonetic and speech_text_text_to_phonetic are defined
# similarity_score_percentage, error_details, feedback = detailed_similarity_analysis_and_feedback(refrence_text_phonetic, speech_text_text_to_phonetic)
# if similarity_score_percentage > 0:
#   print(f"Similarity Score: {similarity_score_percentage:.2f}%")
# else:
#   print(f"Similarity Score: 00.00%")
# for error in error_details:
#   print(f"Error Type: {error[0]}, Expected: '{error[2]}', Got: '{error[1]}' at position {error[3]}")
