pkgname=ephemral
pkgver=1.0
pkgrel=1
pkgdesc="This Package will delete files a while after creation. It is used for downloaded files, which are meant to be used temporarily."
arch=('any')
url="https://github.com/aaabdulkarim/ephemeral"
license=('GPL3')

source=("$pkgname-$pkgver.tar.gz::https://example.com/your-package-name/releases/download/v$pkgver/your-package-name-$pkgver.tar.gz")

build() {
    cd "$pkgname-$pkgver"
    python setup.py build
}

package() {
    cd "$pkgname-$pkgver"
    python setup.py install --root="$pkgdir" --optimize=1
}
