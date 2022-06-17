from tokenizers import ByteLevelBPETokenizer
from transformers import GPT2Config, GPT2LMHeadModel, GPT2Tokenizer

TRAIN_BASE = False

paths = ['python_code_text_data.txt']


tokenizer = ByteLevelBPETokenizer()

if TRAIN_BASE:
    
    tokenizer.train(files=paths, vocab_size=52_000, min_frequency=2, special_tokens=[
        "<s>",
        "<pad>",
        "</s>",
        "unk",
        "<mask>",
    ])

    tokenizer.save_model("tokenizer")


inp = "print('hello world')"
tokenizer = GPT2Tokenizer.from_pretrained('tokenizer')
