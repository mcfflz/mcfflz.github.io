# Qwen3:0.6B

## modelscope 下载模型

```cmd
pip install modelscope --upgrade
cd d:\Codes\Qwen3-0.6B
modelscope download --model Qwen/Qwen3-0.6B --local_dir ./Qwen3-0.6B
```

## transformer 调用

```python
from modelscope import AutoModelForCausalLM, AutoTokenizer

# 模型路径
model_name = "d:\\Codes\\Qwen/Qwen3-0.6B"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    enable_thinking=True # Switches between thinking and non-thinking modes. Default is True.
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)
print("content:", content)
```

## ollama 调用

下载 ollama 安装可执行文件

```html
https://ollama.com/download
```

运行安装文件，安装 ollama 到指定目录（默认在 C 盘下当前用户目录）

```cmd
OllamaSetup.exe /DIR="d:\some\location"
```

到 ollama 库中查看支持的模型，以 qwen3:0.6B 举例，执行：

```cmd
# 也可以单独下载模型
# ollama pull qwen3:0.6B
ollama run qwen3:0.6B
```

如果模型还未下载，则会自动下载该模型。

查看已经安装的模型。

```cmd
ollama list
```

可以通过命令行交互，也可以通过代码调用：

```python
from ollama import chat
from ollama import ChatResponse

st = time.time()
response: ChatResponse = chat(model='qwen3:0.6B', messages=[
  {
    'role': 'user',
    'content': '好久不见。',
  },
])
ed = time.time()
# 打印响应内容
print(response['message']['content'])

print("st: " + str(st))
print("ed: " + str(ed))
print("cost time: " +str(ed-st) + "s")
```

## vllm 调用

下载安装 vllm

```cmd
pip install vllm
```

启动 vllm

# VoiceSenceSmall

## modelscope 下载模型



```cmd
git clone https://
modelscope download --model voicesence --local_dir ./iic/VoiceSenceSmall
```

# paraformer-zh-streaming

modelscope 下载模型

```cmd
```

# FunASR

FunASR 不是模型，而是调用的工具包。

```cmd
pip install funasr --upgrade
```

