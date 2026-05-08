python -m gradient \
    --device="cuda:2" \
    --dtype=32 \
    --epoch=1 \
    --batch_size=2 \
    --effective_batch_size=8 \
    --is_shuffle=False \
    --num_workers=4 \
    --prefetch_factor=8 \
    train

