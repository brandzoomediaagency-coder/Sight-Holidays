
import os

file_path = r'c:\Users\finee\Desktop\New folder\Slight Holidays\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Search for the lines to replace
# We know they are around line 1300
start_idx = -1
for i, line in enumerate(lines):
    if 'document.querySelectorAll(\'a[href^="#"]\').forEach' in line:
        start_idx = i
        break

if start_idx != -1:
    # Keep up to the smooth scroll logic start
    new_content = lines[:start_idx]
    
    # Add the fixed logic
    fixed_logic = """        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>

    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>

    <script>
        // Initialize Swiper
        const swiper = new Swiper('.jaipur-swiper', {
            loop: true,
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
        });

        // Modal Logic
        const modal = document.getElementById('bookingModal');
        let currentPackage = "";

        function openModal(packageName, imageUrl) {
            currentPackage = packageName;
            document.getElementById('modalTitle').innerText = `Price Request for (${packageName})`;
            if (imageUrl) {
                document.getElementById('modalImage').src = imageUrl;
            }
            modal.style.display = "flex";
        }

        function closeModal() {
            modal.style.display = "none";
        }

        window.onclick = function (event) {
            if (event.target == modal) {
                closeModal();
            }
        }

        // Form submission to WhatsApp
        document.getElementById('bookingForm').addEventListener('submit', function (e) {
            e.preventDefault();

            const name = document.getElementById('custName').value;
            const email = document.getElementById('custEmail').value;
            const phone = document.getElementById('custPhone').value;
            const comments = document.getElementById('custComments').value;

            const whatsappNumber = "919811994646";
            const message = `*Price Request from Sight Holidays*%0A%0A` +
                `*Package:* ${currentPackage}%0A` +
                `*Name:* ${name}%0A` +
                `*Email:* ${email}%0A` +
                `*Phone:* +91 ${phone}%0A` +
                `*Comments:* ${comments}`;

            const whatsappUrl = `https://wa.me/${whatsappNumber}?text=${message}`;

            window.open(whatsappUrl, '_blank');
            closeModal();
            this.reset();
        });
    </script>
</body>

</html>
"""
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
        f.write(fixed_logic)
    print("Successfully fixed index.html")
else:
    print("Could not find start of smooth scroll logic")
