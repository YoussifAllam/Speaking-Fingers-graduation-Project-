import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from .detailed_similarity_analysis import detailed_similarity_analysis_and_feedback
import re
import eng_to_ipa as ipa

def clean_text(text):
    lowercased_text = text.lower()
    cleaned_text = re.sub(r'[^a-z0-9\s]', '', lowercased_text)
    return cleaned_text


def speech_to_text(audio_path):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

    model_id = "openai/whisper-large-v3"

    model = AutoModelForSpeechSeq2Seq.from_pretrained(
        model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
    ).to(device)

    processor = AutoProcessor.from_pretrained(model_id)

    pipe = pipeline(
        "automatic-speech-recognition",
        model=model,
        tokenizer=processor.tokenizer,
        feature_extractor=processor.feature_extractor,
        max_new_tokens=128,
        chunk_length_s=30,
        batch_size=16,
        return_timestamps=True,
        torch_dtype=torch_dtype,
        device=device,
    )

    result = pipe(audio_path, generate_kwargs={"language": "english"})
    print(result["text"])
    return clean_text(result["text"])



def text_to_phonetic(text):
    phonetic_transcription = ipa.convert(text)
    return phonetic_transcription


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









