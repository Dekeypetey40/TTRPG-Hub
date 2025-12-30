/**
 * Auth Forms Enhancement Script
 * Handles password visibility toggle, strength indicator, and form validation
 */

document.addEventListener("DOMContentLoaded", function () {
  // ==========================================
  // Password Visibility Toggle
  // ==========================================
  const passwordToggles = document.querySelectorAll(".password-toggle");

  passwordToggles.forEach((toggle) => {
    toggle.addEventListener("click", function () {
      const targetId = this.getAttribute("data-target");
      const passwordInput = document.getElementById(targetId);
      const icon = this.querySelector("i");

      if (passwordInput.type === "password") {
        passwordInput.type = "text";
        icon.classList.remove("fa-eye");
        icon.classList.add("fa-eye-slash");
      } else {
        passwordInput.type = "password";
        icon.classList.remove("fa-eye-slash");
        icon.classList.add("fa-eye");
      }
    });
  });

  // ==========================================
  // Password Strength Indicator
  // ==========================================
  const password1Input = document.getElementById("id_password1");
  const strengthContainer = document.getElementById("password-strength");

  if (password1Input && strengthContainer) {
    password1Input.addEventListener("input", function () {
      const password = this.value;
      const strength = calculatePasswordStrength(password);
      updateStrengthIndicator(strength);
    });
  }

  function calculatePasswordStrength(password) {
    let strength = 0;

    if (password.length === 0) {
      return { score: 0, text: "", width: 0, className: "" };
    }

    // Length check
    if (password.length >= 8) strength += 25;
    if (password.length >= 12) strength += 25;

    // Contains lowercase
    if (/[a-z]/.test(password)) strength += 12.5;

    // Contains uppercase
    if (/[A-Z]/.test(password)) strength += 12.5;

    // Contains numbers
    if (/\d/.test(password)) strength += 12.5;

    // Contains special characters
    if (/[^a-zA-Z0-9]/.test(password)) strength += 12.5;

    let text = "";
    let className = "";

    if (strength < 40) {
      text = "Weak";
      className = "strength-weak";
    } else if (strength < 70) {
      text = "Medium";
      className = "strength-medium";
    } else {
      text = "Strong";
      className = "strength-strong";
    }

    return {
      score: strength,
      text: text,
      width: strength,
      className: className,
    };
  }

  function updateStrengthIndicator(strength) {
    if (strength.score === 0) {
      strengthContainer.innerHTML = "";
      return;
    }

    strengthContainer.innerHTML = `
            <div class="strength-bar ${strength.className}" style="width: ${strength.width}%"></div>
            <div class="strength-text ${strength.className} mt-1">
                <small>Password strength: ${strength.text}</small>
            </div>
        `;
  }

  // ==========================================
  // Form Submission Loading State
  // ==========================================
  const authForms = document.querySelectorAll("#signup-form, #login-form");

  authForms.forEach((form) => {
    form.addEventListener("submit", function (e) {
      const submitBtn = this.querySelector('button[type="submit"]');
      const btnText = submitBtn.querySelector(".btn-text");
      const btnSpinner = submitBtn.querySelector(".btn-spinner");

      // Show loading state
      btnText.classList.add("d-none");
      btnSpinner.classList.remove("d-none");
      submitBtn.disabled = true;
    });
  });

  // ==========================================
  // Input Focus Animation
  // ==========================================
  const formInputs = document.querySelectorAll(
    '.auth-card input[type="text"], .auth-card input[type="email"], .auth-card input[type="password"]'
  );

  formInputs.forEach((input) => {
    input.addEventListener("focus", function () {
      this.parentElement.classList.add("input-focused");
    });

    input.addEventListener("blur", function () {
      this.parentElement.classList.remove("input-focused");
    });
  });

  // ==========================================
  // Real-time Validation Feedback
  // ==========================================
  const signupForm = document.getElementById("signup-form");

  if (signupForm) {
    const password1 = document.getElementById("id_password1");
    const password2 = document.getElementById("id_password2");

    if (password2) {
      password2.addEventListener("input", function () {
        if (password1.value && password2.value) {
          if (password1.value === password2.value) {
            password2.classList.remove("is-invalid");
            password2.classList.add("is-valid");
          } else {
            password2.classList.remove("is-valid");
            password2.classList.add("is-invalid");
          }
        } else {
          password2.classList.remove("is-valid", "is-invalid");
        }
      });
    }
  }

  // ==========================================
  // Add Bootstrap classes to form fields
  // ==========================================
  const allFormInputs = document.querySelectorAll(
    "#signup-form input, #login-form input"
  );

  allFormInputs.forEach((input) => {
    if (
      !input.classList.contains("form-check-input") &&
      input.type !== "hidden"
    ) {
      input.classList.add("form-control");
    }
    if (input.type === "checkbox") {
      input.classList.add("form-check-input");
    }
  });

  console.log("Auth forms enhancement loaded successfully");
});
