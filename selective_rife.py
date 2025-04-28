import torch, cv2, os
from model.RIFE_HDv3 import Model

model = Model()
model.load_model("train_log")  # Téléchargez les poids depuis https://github.com/megvii-research/ECCV2022-RIFE
model.device("hip")  # Force l'utilisation du GPU AMD

def interpolate(img0, img1, num_frames):
    img0 = torch.from_numpy(img0).permute(2,0,1).unsqueeze(0).float().to("hip") / 255.
    img1 = torch.from_numpy(img1).permute(2,0,1).unsqueeze(0).float().to("hip") / 255.
    
    preds = model.multi_inference(img0, img1, num_frames)
    return [(p[0].permute(1,2,0).cpu().numpy() * 255).astype("uint8") for p in preds]

with open("corrupted.txt") as f:
    corrupted = sorted(list(map(int, f.read().split(","))))

for i in range(len(corrupted)-1):
    start, end = corrupted[i], corrupted[i+1]
    gap = end - start - 1
    
    if gap <= 0:
        continue
    
    frame_before = cv2.imread(f"frames/{start:04d}.png")
    frame_after = cv2.imread(f"frames/{end:04d}.png")
    
    generated = interpolate(frame_before, frame_after, gap)
    
    for j, img in enumerate(generated):
        cv2.imwrite(f"frames/{start + j + 1:04d}.png", img)