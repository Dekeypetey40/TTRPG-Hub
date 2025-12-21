from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from cloudinary.uploader import upload as cl_upload
from blog.models import Post

POSTS = [
    {
        "title": "5 Session Zero Tips for a Smooth Campaign",
        "tags": ["GM Tips", "Session Zero", "D&D"],
        "image_url": "https://images.unsplash.com/photo-1542751371-adc38448a05e",
        "content": """
<p>Session zero sets the tone for the entire campaign. Here are five quick wins:</p>
<ol>
  <li><strong>Agree on tone & lines/veils:</strong> Decide the vibe (heroic, grim, gonzo) and use safety tools.</li>
  <li><strong>Table logistics:</strong> When/where, late policy, how to handle absence, and recap duty.</li>
  <li><strong>Character hooks:</strong> Tie PCs together—shared goals, bonds, or debts.</li>
  <li><strong>Rules clarifications:</strong> Variant flanking? Crit rules? Homebrew allowed? Document it.</li>
  <li><strong>Pitch the first arc:</strong> One paragraph of the opening situation to spark ideas.</li>
</ol>
<p>Do this once and you’ll save yourself ten “meta” conversations later.</p>
""",
    },
    {
        "title": "Beginner’s Guide to Building Memorable NPCs",
        "tags": ["GM Tips", "Worldbuilding"],
        "image_url": "https://images.unsplash.com/photo-1600093463592-9dba2c5de0bb",
        "content": """
<p>Great NPCs don’t need a novel. Use the 3×3:</p>
<ul>
  <li><strong>3 Traits:</strong> a voice quirk, a desire, a visible habit.</li>
  <li><strong>3 Connections:</strong> who they trust, fear, and owe.</li>
  <li><strong>3 Scenes:</strong> one intro, one twist, one payoff.</li>
</ul>
<p>Write them on a sticky. When in doubt: <em>what would they do to get what they want?</em></p>
""",
    },
    {
        "title": "Battle Maps on a Budget: Free Tools You Can Use Today",
        "tags": ["Tools", "VTT", "Maps"],
        "image_url": "https://images.unsplash.com/photo-1526318472351-bc6c9f6f5b9c",
        "content": """
<p>You don’t need a subscription to build good maps:</p>
<ul>
  <li><strong>Owlbear Rodeo:</strong> zero-friction VTT for quick fights.</li>
  <li><strong>Dungeondraft (trial) or Inkarnate (free tier):</strong> fast map creation.</li>
  <li><strong>2-Minute Tabletop:</strong> CC-friendly assets for drop-in scenes.</li>
</ul>
<p>Keep it readable: clear walls, doors, cover, and elevation. Don’t over-detail.</p>
""",
    },
    {
        "title": "D&D 5e vs. Pathfinder 2e — Which Fits Your Table?",
        "tags": ["D&D", "Pathfinder 2e", "Advice"],
        "image_url": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da",
        "content": """
<p>Two excellent games, different personalities:</p>
<table class="table">
  <thead><tr><th>5e</th><th>PF2e</th></tr></thead>
  <tbody>
    <tr><td>Loose, rulings-friendly</td><td>Tight math, tactical clarity</td></tr>
    <tr><td>Fast to teach</td><td>Crunchy builds & teamwork shine</td></tr>
    <tr><td>Great for broad fantasy</td><td>Great for tactical set-pieces</td></tr>
  </tbody>
</table>
<p>Your table’s taste > internet discourse. Try a 3-session mini to sample both.</p>
""",
    },
    {
        "title": "Safety Tools that Improve Horror RPGs",
        "tags": ["Horror", "Safety Tools", "GM Tips"],
        "image_url": "https://images.unsplash.com/photo-1519681393784-d120267933ba",
        "content": """
<p>Horror hits harder when everyone feels safe:</p>
<ul>
  <li><strong>Lines & Veils:</strong> set hard limits and fade-to-black topics.</li>
  <li><strong>X / N / O Cards:</strong> adjust intensity in the moment without derailing.</li>
  <li><strong>Pause / Debrief:</strong> check-in breaks and short cool-down chat after sessions.</li>
</ul>
<p>These tools aren’t brakes; they’re traction.</p>
""",
    },
]

class Command(BaseCommand):
    help = "Seed sample TTRPG blog posts with Cloudinary images"

    def add_arguments(self, parser):
        parser.add_argument("--author", type=str, help="Username to assign as author (defaults to first superuser)")
        parser.add_argument("--overwrite", action="store_true", help="Update if a post with same slug exists")

    def handle(self, *args, **opts):
        User = get_user_model()
        author = None
        if opts.get("author"):
            author = User.objects.filter(username=opts["author"]).first()
        if not author:
            author = User.objects.filter(is_superuser=True).first()

        if not author:
            self.stderr.write("No author found. Create a user or pass --author <username>.")
            return

        created = 0
        for p in POSTS:
            slug = slugify(p["title"])
            exists = Post.objects.filter(slug=slug).exists()
            if exists and not opts["overwrite"]:
                self.stdout.write(self.style.WARNING(f"Skipping existing: {p['title']}"))
                continue

            # Upload to Cloudinary (remote URL) and save public_id on the field
            upload_res = cl_upload(
                p["image_url"],
                folder="ttrpghub/seeds",
                overwrite=True,
                unique_filename=True,
                resource_type="image",
            )

            post, _ = Post.objects.update_or_create(
                slug=slug,
                defaults={
                    "title": p["title"],
                    "author": author,
                    "content": p["content"],
                    "excerpt": p["content"][:180],
                    "status": 1,  # Published
                },
            )
            # Save the uploaded image (CloudinaryField stores the public_id)
            post.featured_image = upload_res.get("public_id")
            post.save()
            post.tags.set(p["tags"])
            created += 1

        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created/updated: {created}"))
