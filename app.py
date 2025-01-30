from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AKIRU MAP CODE ORGANIC</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #70e1f5, #ffd194);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            flex-direction: column;
        }

        .header {
            width: 100%;
            padding: 20px;
            text-align: center;
            background-color: #007bff;
            color: white;
            font-size: 30px;
            font-weight: bold;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            border-radius: 0 0 15px 15px;
            margin-bottom: 20px;
        }

        .container {
            width: 95%;
            max-width: 1100px;
            margin: 0;
            padding: 30px;
            background-color: #fff;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            gap: 20px;
        }

        .map-container {
            background: #f9fafb;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 20px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .map-container:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
        }

        .image-container {
            text-align: center;
            margin-bottom: 20px;
        }

        .image-container img {
            width: 100%;
            max-width: 700px;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        }

        .map-code-container {
            padding: 15px;
            background-color: #f2f2f2;
            border-radius: 8px;
            font-size: 15px;
            color: #333;
            word-wrap: break-word;
            margin-bottom: 20px;
            border: 1px solid #ddd;
        }

        .button-container {
            display: flex;
            gap: 20px;
            justify-content: flex-end;
        }

        .button-container button {
            padding: 14px 22px;
            font-size: 16px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
        }

        .button-container button:hover {
            background-color: #0056b3;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }

        .button-container button:focus {
            outline: none;
            box-shadow: 0 0 3px 2px rgba(0, 123, 255, 0.5);
        }

        .scrollable-container {
            max-height: 75vh;
            overflow-y: auto;
            padding-right: 10px;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }

            .map-container {
                padding: 15px;
            }

            .button-container {
                flex-direction: column;
                gap: 10px;
            }

            .button-container button {
                width: 100%;
            }
        }
    </style>
</head>
<body>

    <!-- Header Section with Web Name -->
    <div class="header">
        I SHOW AKIRU
    </div>

    <div class="container">
        <!-- Scrollable Map Details Section -->
        <div class="scrollable-container">
            <!-- Map Details Section 1 -->
            <div class="map-container">
                <div class="image-container">
                    <img src="https://i.postimg.cc/d0XBQRpy/Picsart-24-11-05-08-45-54-713.jpg" alt="Map Image 1">
                </div>
                <div class="map-code-container" id="mapCode1">
                    #FREEFIRE5F17723DB5367E2DCA7B22C2046FE6543235
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode1')">Copy Code</button>
                </div>
            </div>

            <!-- Map Details Section 2 -->
            <div class="map-container">
                <div class="image-container">
                    <img src="https://i.postimg.cc/WpYhWMtB/Picsart-24-12-29-07-27-30-194.jpg" alt="Map Image 2">
                </div>
                <div class="map-code-container" id="mapCode2">
                    #FREEFIRE435DE8FA485D44460958106964C620FC4781
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode2')">Copy Map Code</button>
                </div>
            </div>

            <!-- Map Details Section 3 -->
            <div class="map-container">
                <div class="image-container">
                    <img src="https://i.postimg.cc/XvJBsQ4y/Picsart-24-10-01-12-56-24-762.jpg" alt="Map Image 3">
                </div>
                <div class="map-code-container" id="mapCode3">
                    #FREEFIRE58292AF03367D09884F691E95E9BF1CC4781
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode3')">Copy Map Code🇮🇳</button>
                    <div class="map-code-container" id="mapCode3">
                    #FREEFIREE14D520B849411BE7CFF51E59C32DB658166
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode3')">Copy Map Code🇧🇩</button>
                </div>
            </div>

            <!-- Map Details Section 4 -->
            <div class="map-container">
                <div class="image-container">
                    <img src="https://i.postimg.cc/HL2S8QgL/Free-Fire-01-27-2025-15-30-22.png" alt="Map Image 4">
                </div>
                <div class="map-code-container" id="mapCode4">
                    #FREEFIRE5D55D5D71FB04594BAEFD63D4910B5523235
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode4')">Copy Code 2 player</button>
                    <div class="map-code-container" id="mapCode4">
                    #FREEFIRE68E0F5BDF31FFAD36A2B1F9C80D4A0E23235
                </div>
                <div class="button-container">
                    <button onclick="copyMapCode('mapCode4')">Copy Code 4 player</button>
                </div>
            </div>
            <!-- Map Details Section 5 -->
            <div class="map-container">
                <div class="image-container">
                    <img src="https://i.postimg.cc/HL2S8QgL/Free-Fire-01-27-2025-15-30-22.png" alt="Map Image 5">
                </div>
                <div class="map-code-container" id="mapCode5">
                    #FREEFIRE36E74163DF6B8DB4FAF9A70858CBC1A35872
                </div>
                </div>
            </div>
        </div>
    </div>

    <script>
</body>
</html>
"""

@app.route('/i-show-akiru-all-maps')
def show_maps():
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)
