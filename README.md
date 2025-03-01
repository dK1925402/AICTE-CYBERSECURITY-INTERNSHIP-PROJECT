<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Data Hiding in Image Using Steganography</title>
</head>
<body>
    <h1>Secure Data Hiding in Image Using Steganography</h1>
    <p>
        This project enables users to securely hide and retrieve sensitive information within images using steganography and encryption. It includes a user-friendly GUI for enhanced accessibility and ease of use.
    </p>

    <h2>Features</h2>
    <ul>
        <li><strong>Text Encryption:</strong> Protect sensitive text with password-based encryption.</li>
        <li><strong>Steganography:</strong> Discreetly embed encrypted text within images.</li>
        <li><strong>Graphical User Interface (GUI):</strong> Easy-to-use interface for hiding and retrieving text.</li>
        <li><strong>Two-Layer Security:</strong> Combines encryption and steganography for enhanced protection.</li>
    </ul>

    <h2>Problem Statement</h2>
    <p>
        Traditional methods of data security often expose the presence of sensitive information. This project solves this by securely embedding encrypted data within images, making the data virtually undetectable.
    </p>

    <h2>Technologies Used</h2>
    <ul>
        <li><strong>Python:</strong> Core programming language.</li>
        <li><strong>Pillow:</strong> For image processing.</li>
        <li><strong>Cryptography (Fernet):</strong> For text encryption and decryption.</li>
        <li><strong>Tkinter:</strong> For creating the GUI.</li>
    </ul>

    <h2>How It Works</h2>
    <ol>
        <li><strong>Hiding Data:</strong>
            <ul>
                <li>Upload an image.</li>
                <li>Enter the text to hide and set a password for encryption.</li>
                <li>Save the image with hidden data.</li>
            </ul>
        </li>
        <li><strong>Retrieving Data:</strong>
            <ul>
                <li>Upload the image with hidden data.</li>
                <li>Enter the password to decrypt and reveal the hidden text.</li>
            </ul>
        </li>
    </ol>

    <h2>Wow Factor</h2>
    <ul>
        <li>Seamlessly combines encryption and steganography for dual-layer security.</li>
        <li>Easy-to-use GUI for non-technical users.</li>
        <li>Ensures data remains hidden and safe from unauthorized access.</li>
    </ul>

    <h2>End Users</h2>
    <ul>
        <li>Professionals handling sensitive information.</li>
        <li>Organizations securing confidential data.</li>
        <li>Individuals seeking secure personal communication.</li>
    </ul>

    <h2>Results</h2>
    <p>
        Successfully hides encrypted text in images and retrieves hidden text securely with password authentication.
    </p>

    <h2>Future Scope</h2>
    <ul>
        <li>Add support for hiding larger files like PDFs or documents.</li>
        <li>Implement support for multiple image formats.</li>
        <li>Introduce advanced encryption algorithms for greater security.</li>
    </ul>

    <h2>How to Use</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/your-username/secure-data-hiding.git</code></pre>
        </li>
        <li>Install the required dependencies:
            <pre><code>pip install pillow cryptography</code></pre>
        </li>
        <li>Run the application:
            <pre><code>python main.py</code></pre>
        </li>
    </ol>

    <h2>GitHub Link</h2>
    <p>
        <a href="https://github.com/your-username/secure-data-hiding">Secure Data Hiding in Image Using Steganography</a>
    </p>
</body>
</html>
