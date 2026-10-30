import sys
import json

class ThemeHarmonizer:
    @staticmethod
    def _hex_to_rgb(hex_code):
        h = hex_code.lstrip("#")
        return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

    @classmethod
    def contrast_ratio(cls, hex1, hex2):
        def rel_lum(rgb):
            s = [c / 255.0 for c in rgb]
            lin = [(c / 12.92) if c <= 0.03928 else (((c + 0.055) / 1.055) ** 2.4) for c in s]
            return 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]

        l1 = rel_lum(cls._hex_to_rgb(hex1))
        l2 = rel_lum(cls._hex_to_rgb(hex2))
        return round((max(l1, l2) + 0.05) / (min(l1, l2) + 0.05), 2)

    @classmethod
    def build_theme(cls, brand_hex, font="Inter"):
        bg = "#FFFFFF"
        text = "#0F172A"
        contrast = cls.contrast_ratio(brand_hex, bg)
        return {
            "primary": brand_hex,
            "background": bg,
            "text": text,
            "card_surface": "#F8FAFC",
            "border": "#E2E8F0",
            "font_family": font,
            "contrast_ratio": contrast,
            "is_wcag_aa": contrast >= 4.5
        }

def handle_rpc(request):
    method = request.get("method")
    req_id = request.get("id")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "generate_theme_tokens",
                        "description": "Build accessible theme palette tokens from brand color.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "brand_hex": {"type": "string"},
                                "font": {"type": "string", "default": "Inter"}
                            },
                            "required": ["brand_hex"]
                        }
                    }
                ]
            }
        }

    if method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "generate_theme_tokens":
            res = ThemeHarmonizer.build_theme(args.get("brand_hex", "#2563EB"), args.get("font", "Inter"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_rpc(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "error": {"code": -32000, "message": str(e)}}) + "\n")
            sys.stdout.flush()
