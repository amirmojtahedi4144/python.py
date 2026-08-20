##############  WELCOME TO THE PROFESSIONAL QR CODE GENERATOR ##############
import argparse
import sys
from pathlib import *
from typing import *

import qrcode
from qrcode.image.styledpil import *
from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *


VERSION = "2.0.0"
ERROR_CORRECT_MAP = {
    'L': qrcode.constants.ERROR_CORRECT_L,
    'M': qrcode.constants.ERROR_CORRECT_M,
    'Q': qrcode.constants.ERROR_CORRECT_Q,
    'H': qrcode.constants.ERROR_CORRECT_H,
}


def generate_qr_code(
    data: str,
    output_path: Path,
    box_size: int = 10,
    border: int = 4,
    error_correction: str = 'L',
    fill_color: str = 'black',
    back_color: str = 'white',
    use_rounded: bool = False,
) -> None:
    if not data or not data.strip():
        raise ValueError("Data to encode cannot be empty.")

    if error_correction.upper() not in ERROR_CORRECT_MAP:
        raise ValueError(
            f"Invalid error correction level. Choose from: {', '.join(ERROR_CORRECT_MAP.keys())}"
        )

    if output_path.suffix.lower() != '.png':
        output_path = output_path.with_suffix('.png')

    if output_path.exists():
        raise FileExistsError(
            f"Output file '{output_path}' already exists. Use --force to overwrite."
        )

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_MAP[error_correction.upper()],
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)

        if use_rounded:
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=SolidFillColorMask(
                    back_color=back_color,
                    front_color=fill_color
                )
            )
        else:
            img = qr.make_image(
                fill_color=fill_color,
                back_color=back_color
            )

        img.save(output_path)
        print(f"QR code successfully generated and saved at: {output_path.resolve()}")

    except Exception as e:
        raise IOError(f"Failed to save the QR code image: {e}")


def interactive_mode() -> dict:
    print("\n" + "=" * 50)
    print(" INTERACTIVE QR CODE GENERATOR")
    print("=" * 50)

    data = input("Enter the data to encode (text/URL): ").strip()
    if not data:
        print("Error: Data cannot be empty.")
        sys.exit(1)

    filename = input("Enter the filename (without extension, e.g., 'my_qr'): ").strip()
    if not filename:
        filename = "qrcode"

    custom = input("Do you want to customize colors/size? (y/n): ").strip().lower()
    if custom == 'y':
        fill = input("Fill color (e.g., 'black', '#FF5733'): ") or 'black'
        back = input("Back color (e.g., 'white', '#F0F0F0'): ") or 'white'
        size = int(input("Box size (default 10): ") or 10)
        border = int(input("Border (default 4): ") or 4)
        ec = input("Error correction (L/M/Q/H, default L): ").upper() or 'L'
    else:
        fill, back, size, border, ec = 'black', 'white', 10, 4, 'L'

    return {
        'data': data,
        'filename': filename,
        'fill_color': fill,
        'back_color': back,
        'box_size': size,
        'border': border,
        'error_correction': ec,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Professional QR Code Generator with advanced customization.",
        epilog=f"Example: python qr_gen.py -d 'https://example.com' -o my_qr -fc '#FF0000' --rounded"
    )

    parser.add_argument(
        '-d', '--data',
        type=str,
        help="Data (text or URL) to encode into the QR code."
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default='qrcode',
        help="Output filename (without extension). Default: 'qrcode'"
    )

    parser.add_argument(
        '-s', '--size',
        type=int,
        default=10,
        help="Box size in pixels. Default: 10"
    )
    parser.add_argument(
        '-b', '--border',
        type=int,
        default=4,
        help="Border thickness (number of boxes). Default: 4"
    )
    parser.add_argument(
        '-ec', '--error-correction',
        type=str,
        choices=['L', 'M', 'Q', 'H'],
        default='L',
        help="Error correction level. Default: L (Lowest)"
    )
    parser.add_argument(
        '-fc', '--fill-color',
        type=str,
        default='black',
        help="Fill (foreground) color. Default: black"
    )
    parser.add_argument(
        '-bc', '--back-color',
        type=str,
        default='white',
        help="Background color. Default: white"
    )
    parser.add_argument(
        '--rounded',
        action='store_true',
        help="Enable rounded corners for QR modules (stylized look)."
    )

    parser.add_argument(
        '-f', '--force',
        action='store_true',
        help="Force overwrite if output file already exists."
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'QR Code Generator v{VERSION}'
    )

    args = parser.parse_args()

    if not args.data:
        params = interactive_mode()
        data = params['data']
        output_path = Path(params['filename'])
        box_size = params['box_size']
        border = params['border']
        ec = params['error_correction']
        fill_color = params['fill_color']
        back_color = params['back_color']
        use_rounded = False
        force = False
    else:
        data = args.data
        output_path = Path(args.output)
        box_size = args.size
        border = args.border
        ec = args.error_correction
        fill_color = args.fill_color
        back_color = args.back_color
        use_rounded = args.rounded
        force = args.force

    if output_path.suffix.lower() != '.png':
        output_path = output_path.with_suffix('.png')

    if output_path.exists() and not force:
        try:
            overwrite = input(
                f"File '{output_path}' already exists. Overwrite? (y/n): "
            ).strip().lower()
            if overwrite != 'y':
                print("Operation cancelled by user.")
                sys.exit(0)
        except KeyboardInterrupt:
            print("\n Cancelled.")
            sys.exit(1)

    try:
        generate_qr_code(
            data=data,
            output_path=output_path,
            box_size=box_size,
            border=border,
            error_correction=ec,
            fill_color=fill_color,
            back_color=back_color,
            use_rounded=use_rounded,
        )
        print("\n You can scan this QR code with any standard scanner or smartphone camera.")
        print("Thank you for using the Professional QR Code Generator!")

    except (ValueError, FileExistsError, IOError) as e:
        print(f" Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f" An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()