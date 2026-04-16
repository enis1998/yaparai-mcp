"""Image editing tools — transform, background removal, face swap."""

from __future__ import annotations

from yaparai.client import YaparAIClient


async def transform_image(
    prompt: str,
    image_url: str,
    negative_prompt: str = "",
    width: int = 512,
    height: int = 512,
    style: str | None = None,
) -> dict:
    """
    Transform an existing image using AI (image-to-image).

    Uses the source image as a reference and applies the prompt to create
    a new variation. Great for style transfer, modifications, and enhancements.
    Cost: ~6 credits.

    Args:
        prompt: Description of the desired transformation
        image_url: URL of the source image to transform
        negative_prompt: Things to avoid in the output
        width: Output width in pixels (64-2048, default 512)
        height: Output height in pixels (64-2048, default 512)
        style: Style preset (realistic, anime, cinematic, artistic)

    Returns:
        Dict with image_url, job_id, credits_used, and balance_remaining.
    """
    client = YaparAIClient()
    job = await client.generate({
        "type": "image",
        "mode": "img2img",
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "image_url": image_url,
        "width": width,
        "height": height,
        "style": style,
    })

    result = await client.wait_for_result(job["job_id"], timeout=60)
    return {
        "status": "success",
        "image_url": result.get("result_url"),
        "job_id": result.get("job_id"),
        "credits_used": job.get("credits_used"),
        "balance_remaining": job.get("balance_remaining"),
    }


async def remove_background(
    prompt: str,
    image_url: str,
) -> dict:
    """
    Remove the background from an image using AI.

    Upload an image and get back a version with the background removed
    (transparent or white). Works great for product photos, portraits,
    and any image where you need a clean cutout.
    Cost: ~2 credits.

    Args:
        prompt: Description or instructions (e.g., "remove background, keep the person")
        image_url: URL of the image to process

    Returns:
        Dict with image_url (processed image), job_id, credits_used,
        and balance_remaining.
    """
    client = YaparAIClient()
    job = await client.generate({
        "type": "image",
        "mode": "editor_bg_remove",
        "prompt": prompt,
        "image_url": image_url,
    })

    result = await client.wait_for_result(job["job_id"], timeout=60)
    return {
        "status": "success",
        "image_url": result.get("result_url"),
        "job_id": result.get("job_id"),
        "credits_used": job.get("credits_used"),
        "balance_remaining": job.get("balance_remaining"),
    }


async def swap_face(
    prompt: str,
    image_url: str,
) -> dict:
    """
    Swap a face in an image using AI.

    Provide a source image and instructions for the face swap.
    The AI will replace the face while keeping the rest of the image intact.
    Cost: ~6 credits.

    Args:
        prompt: Instructions for the face swap
        image_url: URL of the image containing the face to swap

    Returns:
        Dict with image_url (result image), job_id, credits_used,
        and balance_remaining.
    """
    client = YaparAIClient()
    job = await client.generate({
        "type": "image",
        "mode": "editor_face_swap",
        "prompt": prompt,
        "image_url": image_url,
    })

    result = await client.wait_for_result(job["job_id"], timeout=60)
    return {
        "status": "success",
        "image_url": result.get("result_url"),
        "job_id": result.get("job_id"),
        "credits_used": job.get("credits_used"),
        "balance_remaining": job.get("balance_remaining"),
    }
