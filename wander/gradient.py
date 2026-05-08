import torch
import torch.nn as nn
from transformers import set_seed
from safetensors.torch import load_file, save_file, load_model, save_model
from torch.utils.data import DataLoader, Dataset
from nu_trainer import NuTrainer
from logab import log_wrap
from fire import Fire
from dataclasses import dataclass

# --- Layer Definitions ---

def init_tensor():
    model = SimpleModel().to(device="cuda", dtype=torch.float32)
    input = torch.randn(16, 2).to(device="cuda", dtype=torch.float32)
    output = torch.randint(0, 8, (16,)).to(device="cuda", dtype=torch.float32)
    io_tensor = {
        "input": input,
        "output": output
    }
    # save_file(model.state_dict(), "model.safetensors")
    # save_file(input, "input.safetensors")
    # save_file(output, "output.safetensors")
    save_file(io_tensor, "io_tensor.safetensors")
    save_file(model.state_dict(), "model.safetensors")
    pass

class SmallDataset(Dataset):
    def __init__(self, device="cpu"):
        super().__init__()
        self.dataset = load_file("io_tensor.safetensors", device=device)
        pass
    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx: int):
        return {
            'input': self.dataset['input'][idx],
            'output': self.dataset['output'][idx],
            'string': ['abc' for x in range(4)]
        }

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear_1 = nn.Linear(2, 4)
        self.act = nn.ReLU()
        self.linear_2 = nn.Linear(4, 4)
        self.lm_head = nn.Linear(4, 8)
     
    def forward(self, input):
        hidden_states = self.linear_1(input)
        hidden_states = self.act(hidden_states)
        hidden_states = self.linear_2(hidden_states)
        output = self.lm_head(hidden_states)
        return output

@dataclass
class SimpleTrainer(NuTrainer):
    my_model:any="abcde"
    # ---------------------------------------------------

    def train(self):
        self.fix_seed()
        model = SimpleModel().to(device=self.device, dtype=self.dtype)
        model_weights = load_file("model.safetensors")
        model.load_state_dict(model_weights)
        for name, param in model.named_parameters():
            if "linear_1" in name:
                param.requires_grad = True
            else:
                param.requires_grad = False
        self.print_trainable(model)
        small_dataset = SmallDataset()
        train_loader = self.create_dataloader(small_dataset)
        for ep in range(self.epoch):
            for idx, batch in enumerate(train_loader):
                batch = self.transfer_tensor(batch)
                print(idx)
                pass
        pass

def train(device="cuda:2", dtype=torch.float32):
    
    model = SimpleModel().to(device=device, dtype=dtype)
    model_weights = load_file("model.safetensors")
    model.load_state_dict(model_weights)

    small_dataset = SmallDataset()
    # input, output = load_file("io_tensors.safetensors")
    small_trainloader = DataLoader(
        small_dataset,
        batch_size=2
    )
    for idx, (input, output) in enumerate(small_trainloader):

        pass
    pass


if __name__ == "__main__":
    with log_wrap(is_format_lib=True):
        Fire(SimpleTrainer)
