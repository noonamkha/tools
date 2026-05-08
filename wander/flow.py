import torch
import torch.nn as nn

# --- Layer Definitions ---

CHOSEN_DTYPE = torch.float32
DEVICE = "cuda"

class LayerA(nn.Module):
    """
    A custom layer that applies weight A.
    It takes two inputs, x_a and x_b, and applies the same
    weight A to both, producing two separate outputs.
    """
    def __init__(self, initial_weight):
        super().__init__()
        # Define A as a trainable parameter, initialized with the given value
        self.A = nn.Parameter(torch.tensor([initial_weight], dtype=CHOSEN_DTYPE))

    def forward(self, x_a):
        """
        Calculates:
        y1_a = A * x_a
        y1_b = A * x_b
        """
        y1_a = self.A * x_a
        return y1_a

class LayerB(nn.Module):
    """
    A custom layer that applies weight B.
    It takes one input, y1_a, and produces one output, y2.
    """
    def __init__(self, initial_weight):
        super().__init__()
        # Define B as a trainable parameter
        self.B = nn.Parameter(torch.tensor([initial_weight], dtype=CHOSEN_DTYPE))

    def forward(self, y1_a):
        """
        Calculates:
        y2 = B * y1_a
        """
        y2 = self.B * y1_a
        return y2

class LayerC(nn.Module):
    """
    A custom layer that applies weight C.
    It takes one input, y2, and produces the final output, y3.
    """
    def __init__(self, initial_weight):
        super().__init__()
        # Define C as a trainable parameter
        self.C = nn.Parameter(torch.tensor([initial_weight], dtype=CHOSEN_DTYPE))

    def forward(self, y2):
        """
        Calculates:
        y3 = C * y2
        """
        y3 = self.C * y2
        return y3

# --- Combined Model Definition ---

class SimpleModel(nn.Module):
    """
    Combines the three layers A, B, and C into a single model.
    The forward pass orchestrates the flow of data through the layers
    as you defined.
    """
    def __init__(self, weight_A, weight_B, weight_C):
        super().__init__()
        # Instantiate each custom layer with its initial weight
        self.layer_A = LayerA(weight_A)
        self.layer_B = LayerB(weight_B)
        self.layer_C = LayerC(weight_C)

    def forward(self, x_a):
        """
        Runs the full forward pass:
        1. (x_a, x_b) -> LayerA -> (y1_a, y1_b)
        2. y1_a -> LayerB -> y2
        3. y2 -> LayerC -> y3
        Returns the outputs needed for the custom loss calculation.
        """
        # Layer 1 outputs
        y1_a = self.layer_A(x_a)
        
        # Layer 2 output
        y2 = self.layer_B(y1_a)
        
        # Layer 3 output
        y3 = self.layer_C(y2)
        
        # Return all outputs needed to compute the total loss
        return y3

# --- Main execution script ---
if __name__ == "__main__":
    
    # 1. Define initial weights and inputs
    A_val = 0.5
    B_val = -0.4
    C_val = 0.8
    
    # Define inputs and target as PyTorch tensors
    x_a = torch.tensor([0.3], dtype=CHOSEN_DTYPE, device=DEVICE)
    x_b = torch.tensor([0.2], dtype=CHOSEN_DTYPE, device=DEVICE)
    y_target = torch.tensor([1.2], dtype=CHOSEN_DTYPE, device=DEVICE)

    # 2. Instantiate the model
    model = SimpleModel(A_val, B_val, C_val).to(dtype=CHOSEN_DTYPE, device=DEVICE)

    # 3. Perform the forward pass
    print("--- Forward Pass ---")
    # Get the outputs from the model
    y3 = model(x_a)
    y1_a = model.layer_A(x_a)
    # y1_b = model.layer_A(x_b)
    with torch.no_grad():
        y1_b = model.layer_A(x_b)
    
    # We can also get y2 for demonstration
    # Note: We re-calculate y2 here just for printing.
    # In a real scenario, you might not need to expose it.
    y2_intermediate = model.layer_B(y1_a) 
    
    print(f"Inputs: x_a = {x_a.item():.3f}, x_b = {x_b.item():.3f}")
    print(f"Target: y = {y_target.item():.3f}")
    print("-" * 20)
    print(f"Weights: A = {model.layer_A.A.item():.3f}, B = {model.layer_B.B.item():.3f}, C = {model.layer_C.C.item():.3f}")
    print("-" * 20)
    print(f"y1_a (A * x_a) = {y1_a.item():.4f}")
    print(f"y1_b (A * x_b) = {y1_b.item():.4f}")
    print(f"y2 (B * y1_a) = {y2_intermediate.item():.4f}")
    print(f"y3 (C * y2)   = {y3.item():.4f}")

    # 4. Calculate the custom loss
    print("\n--- Loss Calculation ---")
    
    # We can use nn.MSELoss, which calculates (input - target)^2
    loss_fn_mse = nn.MSELoss()
    
    # L1 = (y - y3)^2
    # Note: MSELoss(a, b) is (a - b)^2. So we can pass (y3, y_target).
    L1 = loss_fn_mse(y3, y_target)
    
    # L2 = (y1_b - y1_a)^2
    # L2 = loss_fn_mse(y1_a, y1_b)
    L2 = y1_a*y1_b
    
    # Final loss: L = L1 + L2
    L = L1 + L2

    print(f"L1 (y3 - y_target)^2 = {L1.item():.6f}")
    print(f"L2 (y1_b - y1_a)^2 = {L2.item():.6f}")
    print(f"Total Loss (L = L1 + L2) = {L.item():.6f}")

    # 5. Perform backward pass (Calculate Gradients)
    print("\n--- Backward Pass (Gradients) ---")
    
    # Clear any previously calculated gradients
    model.zero_grad()
    
    # Calculate the gradients of the Total Loss L
    # with respect to all parameters (A, B, C)
    L.backward()

    # Access and print the gradients
    print(f"Gradient of L w.r.t. A (dL/dA): {model.layer_A.A.grad.item():.6f}")
    print(f"Gradient of L w.r.t. B (dL/dB): {model.layer_B.B.grad.item():.6f}")
    print(f"Gradient of L w.r.t. C (dL/dC): {model.layer_C.C.grad.item():.6f}")
