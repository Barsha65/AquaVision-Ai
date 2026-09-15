import numpy as np


def white_balance(image: np.ndarray) -> np.ndarray:
    """Apply gray-world white balance to an RGB image."""

    if image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Expected an RGB image with shape (H, W, 3).")

    R=image[:,:,0]
    G=image[:,:,1]
    B=image[:,:,2]

    R_mean = np.mean(R)
    G_mean = np.mean(G)
    B_mean = np.mean(B)
    target = (R_mean + G_mean + B_mean) / 3
    if R_mean == 0 or G_mean == 0 or B_mean == 0:
        raise ValueError("Cannot apply white balance when a channel mean is zero.")

    scale_R=target/R_mean
    scale_G=target/G_mean
    scale_B=target/B_mean

    adjusted_R=R*scale_R
    adjusted_B=B*scale_B
    adjusted_G=G*scale_G

    balanced=np.stack([adjusted_R,adjusted_G,adjusted_B],axis=2)
    clip=np.clip(balanced,0,255)
    clip=clip.astype(np.uint8)
    return clip