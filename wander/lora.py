import torch
import torch.nn as nn
from mini.random_seed import fix_seed
print("import trans")
from transformers import PreTrainedModel, PretrainedConfig
from safetensors.torch import load_model, save_model

print("import peft")
from peft import (
    LoraConfig,
    get_peft_model,
    PeftModel,
    AutoPeftModel,
    PeftConfig
)



print("done import")
class MyPretrained(PreTrainedModel):
    def __init__(self, config: PretrainedConfig = PretrainedConfig()):
        super().__init__(config)
        self.layer_1 = nn.Linear(3,4, bias=False)
        self.layer_2 = nn.Linear(4,3, bias=False)
        self.layer_3 = nn.Linear(3,1, bias=False)

    def get_layer_1(self, x):
        return self.layer_1(x)

    def get_layer_2(self, x):
        return self.layer_2(x)

    def get_layer_3(self, x):
        return self.layer_3(x)

    def forward(self, x):
        x1 = self.get_layer_1(x)
        x1_ori = torch.matmul(x, self.layer_1.weight.T)
        x2 = self.get_layer_2(x1)
        x2_ori = torch.matmul(x1, self.layer_2.weight.T)
        x3 = self.get_layer_3(x2)
        x3_ori = torch.matmul(x2, self.layer_3.weight.T)
        return x1, x2, x3, x1_ori, x2_ori, x3_ori
    


class MyPytorch(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(3,4, bias=False)
        self.layer_2 = nn.Linear(4,3, bias=False)
        self.layer_3 = nn.Linear(3,1, bias=False)
        self.layer_x = nn.Linear

    def get_layer_1(self, x):
        return self.layer_1(x)

    def get_layer_2(self, x):
        return self.layer_2(x)

    def get_layer_3(self, x):
        return self.layer_3(x)

    def forward(self, x):
        x1 = self.get_layer_1(x)
        x1_ori = torch.matmul(x, self.layer_1.weight.T)
        x2 = self.get_layer_2(x1)
        x2_ori = torch.matmul(x1, self.layer_2.weight.T)
        x3 = self.get_layer_3(x2)
        x3_ori = torch.matmul(x2, self.layer_3.weight.T)
        return x1, x2, x3, x1_ori, x2_ori, x3_ori

def init_lora():
    pytorch_lora = get_peft_model(pytorch_lora, lora_config)
    pretrained_lora = get_peft_model(pretrained_lora, lora_config)


if __name__ == "__main__":
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
    DTYPE = torch.float32
    fix_seed()
    torch.set_printoptions(profile="full")

    inputs = torch.rand(1,3).to(device=DEVICE, dtype=DTYPE)

    pretrained_config = PretrainedConfig()
    lora_config = LoraConfig(
        r=2,
        target_modules= ['layer_1'],
        lora_alpha=2,
        lora_dropout=0.05,
        init_lora_weights=False
    )

    pytorch_lora_config = PeftConfig.from_pretrained("/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pytorch_lora")
    pretrained_lora_config = PeftConfig.from_pretrained("/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pretrained_lora")
    
    pytorch_base = MyPytorch().to(device=DEVICE, dtype=DTYPE)
    pytorch_lora = MyPytorch().to(device=DEVICE, dtype=DTYPE)

    
    # pytorch_lora = get_peft_model(pytorch_lora, peft_config=lora_config)
    # pytorch_lora.save_pretrained("/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pytorch_lora/")

    load_model(pytorch_base, "/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pytorch_base/pytorch_base.safetensors")
    load_model(pytorch_lora, "/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pytorch_base/pytorch_base.safetensors")

    pretrained_base = MyPretrained.from_pretrained("/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pretrained_base", config=pretrained_config, device_map=DEVICE, dtype=DTYPE)
    pretrained_lora = MyPretrained.from_pretrained("/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pretrained_base", config=pretrained_config, device_map=DEVICE, dtype=DTYPE)
    
    pytorch_lora = PeftModel.from_pretrained(pytorch_lora, "/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pytorch_lora", config=pytorch_lora_config, device_map=DEVICE, dtype=DTYPE)
    pretrained_lora = PeftModel.from_pretrained(pretrained_lora, "/hpcfs/users/a1956473/projects/quick-testing/checkpoints/pretrained_lora", config=pytorch_lora_config, device_map=DEVICE, dtype=DTYPE)




    with torch.no_grad():
        pytorch_base.eval()
        pytorch_lora.eval()
        pretrained_base.eval()
        pretrained_lora.eval()


        output_pretrained_base = pretrained_base(inputs)
        output_pretrained_lora = pretrained_lora(inputs)
        output_pytorch_base = pytorch_base(inputs)
        output_pytorch_lora = pytorch_lora(inputs)

        layer1_pytorch_lora = pytorch_lora.layer_1(inputs)
        layer1_pytorch_ori = output_pytorch_lora[3]
        layer1_pytorch_get = pytorch_lora.get_layer_1(inputs)
        x1_pytorch_lora = output_pytorch_lora[3] + torch.matmul(torch.matmul(inputs, pytorch_lora.base_model.model.layer_1.lora_A.default.weight.T),pytorch_lora.base_model.model.layer_1.lora_B.default.weight.T)
        


        layer1_pretrained_lora = pretrained_lora.layer_1(inputs)
        layer1_pretrained_ori = output_pretrained_lora[3]
        layer1_pretrained_get = pretrained_lora.get_layer_1(inputs)
        x1_pretrained_lora = output_pretrained_lora[3] + torch.matmul(torch.matmul(inputs, pretrained_lora.base_model.model.layer_1.lora_A.default.weight.T),pretrained_lora.base_model.model.layer_1.lora_B.default.weight.T)
        
        pass