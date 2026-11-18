import app as app_module
import audit

CREATOR_ID = "test_cost"
# TEXT = "The quick brown fox jumps over the lazy dog."
TEXT = "Last weekend I finally cleaned out the garage, something I had been avoiding for almost two years. I started early in the morning with a cup of coffee and a plan to sort everything into three piles: keep, donate, and throw away. The plan lasted about ten minutes. Almost immediately I found a box of old photographs, and I sat on the concrete floor for an hour looking at pictures from college trips I had completely forgotten. Behind the photos was my old bicycle, covered in dust, with both tires flat. I decided to fix it instead of tossing it, so I drove to the hardware store and bought a pump, new inner tubes, and a small can of oil. By the afternoon the chain was moving smoothly again, and I took a short ride around the neighborhood. The garage was still a mess when the sun went down, but I did not mind very much. Still, it felt good to make some progress. I had rediscovered something I loved, and I promised myself that next weekend I would finish the job properly, maybe with a friend to help and a playlist of loud music to keep us moving along."
N_TRIALS = 5
client = app_module.app.test_client()

for i in range(N_TRIALS):
    resp = client.post("/submit", json={"creator_id": CREATOR_ID, "text": TEXT})

rows = audit.read_entries(N_TRIALS)

total_time = 0
for row in rows:
    total_time += row.get("duration_ms")

avg_time = total_time / N_TRIALS
print(f"total_time: {total_time}")
print(f"avg_time: {avg_time} ms")
print(f"avg_time: {avg_time/1000} s")
