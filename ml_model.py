from tokenizers import ByteLevelBPETokenizer
from transformers import GPT3Config, GPT3LMHeadModel, GPT3Tokenizer

TRAIN_BASE = False
paths = ["python_code_text_data.txt"]
if TRAIN_BASE:
    tokenizer = ByteLevelBPETokenizer()
    tokenizer.train(files=paths, vocab_size=52000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "<unk>",
        "<mask>",
    ])
    tokenizer.save_model("tokenizer")

inp = 'print("hello world")'

tokenizer = GPT3Tokenizer.from_pretrained('tokenizer')

tokenizer.add_special_token({
    "eos_token": "</s>",
    "bos_tooken": "<s>",
    "unk_token": "<unk>",
    "pad_token": "<pad>",
    "mask_token": "<mask>"
})

t = tokenizer.encode(inp)
print(t)
print(tokenizer.decode(t))

config = GPT3Config(
    vocab_size=tokenizer.vocab_size,
    bos_token=tokenizer.bos_token_id,
    eos_token=tokenizer.eos_token_id
)

model = GPT3LMHeadModel.from_pretrained("GPyT").to("cuda")

while True:
    inp = input(">>> ")
    input_ids = tokenizer.encode(inp, return_tensors='pt').to("cuda")
    beam_output = model.generate(
        input_ids,
        max_length=512,
        num_beams=10,
        temperature=0.7,
        no_repeat_ngram_size=5,
        num_return_sequences=1,
    )
    for beam in beam_output:
        out = tokenizer.decode(beam)
        fout = out.replace("<N>", "\n")
