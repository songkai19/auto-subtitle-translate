import time
import openai


# API_KEY = "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"
API_KEY = "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"
MODEL = "gpt-3.5-turbo"
MODEL_GPT3 = "text-davinci-003"
WORKER_DELAY_DURATION = 0.2
ONE_LINE_WORDS_LIMIT = 30


def line_tt(transcript_line):
    openai.api_key = API_KEY

    refinedSegment = f"{transcript_line['text'].strip().replace('-->', '->')}"

    # response = openai.ChatCompletion.create(
    #     model=MODEL,
    #     messages=[
    #         {"role": "system", "content": "You are a helpful assistant that translates English to Simple Chinese."},
    #         {"role": "user", "content": f"Translate the English text content into Simple Chinese:\n \"{refinedSegment}\""},
    #     ],
    #     temperature=0,
    # )

    response = openai.Completion.create(
        model=MODEL_GPT3,
        prompt=f"Translate the English text content into Simple Chinese without period:\n \"{refinedSegment}\"",
        temperature=0,
        max_tokens=2048,
        # top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    time.sleep(WORKER_DELAY_DURATION)
    
    # result = response['choices'][0]['message']['content']
    result = response['choices'][0]['text']

    words_count = len(result)
    if words_count > ONE_LINE_WORDS_LIMIT :
        half_line = words_count//2
        result = f"{result[slice(half_line)]}\n{result[slice(half_line+1, words_count)]}"

    transcript_line['text'] = result
    # print(transcript_line)
    return transcript_line
