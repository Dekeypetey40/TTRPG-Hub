from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.html import strip_tags
from blog.models import Post

POSTS = [
    {
        "title": "5 Session Zero Tips for a Smooth Campaign",
        "tags": ["GM Tips", "Session Zero", "D&D"],
        "content": """
<p>Session zero sets the tone for the entire campaign. Here are five quick wins:</p>
<ol>
  <li><strong>Agree on tone & lines/veils:</strong> Decide the vibe (heroic, grim, gonzo) and use safety tools.</li>
  <li><strong>Table logistics:</strong> When/where, late policy, how to handle absence, and recap duty.</li>
  <li><strong>Character hooks:</strong> Tie PCs together—shared goals, bonds, or debts.</li>
  <li><strong>Rules clarifications:</strong> Variant flanking? Crit rules? Homebrew allowed? Document it.</li>
  <li><strong>Pitch the first arc:</strong> One paragraph of the opening situation to spark ideas.</li>
</ol>
<p>Do this once and you'll save yourself ten "meta" conversations later.</p>
""",
    },
    {
        "title": "Beginner's Guide to Building Memorable NPCs",
        "tags": ["GM Tips", "Worldbuilding"],
        "content": """
<p>Great NPCs don't need a novel. Use the 3×3:</p>
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
        "content": """
<p>You don't need a subscription to build good maps:</p>
<ul>
  <li><strong>Owlbear Rodeo:</strong> zero-friction VTT for quick fights.</li>
  <li><strong>Dungeondraft (trial) or Inkarnate (free tier):</strong> fast map creation.</li>
  <li><strong>2-Minute Tabletop:</strong> CC-friendly assets for drop-in scenes.</li>
</ul>
<p>Keep it readable: clear walls, doors, cover, and elevation. Don't over-detail.</p>
""",
    },
    {
        "title": "D&D 5e vs. Pathfinder 2e — Which Fits Your Table?",
        "tags": ["D&D", "Pathfinder 2e", "Advice"],
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
<p>Your table's taste > internet discourse. Try a 3-session mini to sample both.</p>
""",
    },
    {
        "title": "Safety Tools that Improve Horror RPGs",
        "tags": ["Horror", "Safety Tools", "GM Tips"],
        "content": """
<p>Horror hits harder when everyone feels safe:</p>
<ul>
  <li><strong>Lines & Veils:</strong> set hard limits and fade-to-black topics.</li>
  <li><strong>X / N / O Cards:</strong> adjust intensity in the moment without derailing.</li>
  <li><strong>Pause / Debrief:</strong> check-in breaks and short cool-down chat after sessions.</li>
</ul>
<p>These tools aren't brakes; they're traction.</p>
""",
    },
]

class Command(BaseCommand):
    help = "Seed sample TTRPG blog posts for local development (no images needed)"

    def add_arguments(self, parser):
        parser.add_argument("--author", type=str, help="Username to assign as author")
        parser.add_argument("--overwrite", action="store_true", help="Update if a post with same slug exists")

    def handle(self, *args, **opts):
        User = get_user_model()
        author = None
        
        if opts.get("author"):
            author = User.objects.filter(username=opts["author"]).first()
        
        if not author:
            author = User.objects.filter(is_superuser=True).first()

        if not author:
            # Create a default author if none exists
            self.stdout.write(self.style.WARNING("No superuser found. Creating default author..."))
            author = User.objects.create_user(
                username="admin",
                email="admin@example.com",
                password="admin123",
                is_superuser=True,
                is_staff=True
            )
            self.stdout.write(self.style.SUCCESS(f"Created admin user (username: admin, password: admin123)"))

        created = 0
        for p in POSTS:
            slug = slugify(p["title"])
            exists = Post.objects.filter(slug=slug).exists()
            if exists and not opts.get("overwrite"):
                self.stdout.write(self.style.WARNING(f"Skipping existing: {p['title']}"))
                continue

            # Strip HTML tags from content to create clean excerpt
            clean_content = strip_tags(p["content"])
            excerpt = clean_content[:180] + "..." if len(clean_content) > 180 else clean_content
            
            post, was_created = Post.objects.update_or_create(
                slug=slug,
                defaults={
                    "title": p["title"],
                    "author": author,
                    "content": p["content"],
                    "excerpt": excerpt,
                    "status": 1,  # Published
                    # Leave featured_image blank - template will use placeholder
                },
            )
            
            # Add tags
            if p.get("tags"):
                post.tags.set(*[p["tags"]])
            
            created += 1
            action = "Created" if was_created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action}: {p['title']}"))

        self.stdout.write(self.style.SUCCESS(f"\nSeed complete! Created/updated {created} posts."))
        self.stdout.write(self.style.SUCCESS(f"Author: {author.username}"))
        self.stdout.write(self.style.SUCCESS(f"Images: Using placeholder (no Cloudinary needed)"))
        self.stdout.write(self.style.SUCCESS(f"\nVisit: http://localhost:8000"))

