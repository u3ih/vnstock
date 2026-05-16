"""Smoke tests — verify package imports and basic instantiation without network."""

import sys
import pytest


def test_package_imports():
    import vnstock
    assert vnstock is not None


def test_public_api_classes_importable():
    from vnstock import Quote, Listing, Company, Finance, Trading, Fund, Vnstock
    for cls in (Quote, Listing, Company, Finance, Trading, Fund, Vnstock):
        assert cls is not None


def test_constants_importable():
    from vnstock import INDICES_INFO, INDICES_MAP, INDEX_GROUPS, SECTOR_IDS, EXCHANGES
    assert isinstance(EXCHANGES, (list, dict, tuple, set))


def test_auth_functions_importable():
    from vnstock import register_user, change_api_key, check_status
    for fn in (register_user, change_api_key, check_status):
        assert callable(fn)


def test_vnai_not_imported():
    import vnstock  # noqa: F401
    assert "vnai" not in sys.modules, "vnai must not be imported by vnstock"


def test_kbs_explorer_importable():
    from vnstock.explorer.kbs import quote, listing, company, financial, trading
    for mod in (quote, listing, company, financial, trading):
        assert mod is not None


def test_vci_explorer_importable():
    from vnstock.explorer.vci import quote, listing, company, financial, trading
    for mod in (quote, listing, company, financial, trading):
        assert mod is not None


def test_listing_instantiation():
    from vnstock.api.listing import Listing
    listing = Listing(source="VCI", show_log=False)
    assert listing is not None
    assert listing.source.lower() == "vci"


def test_quote_instantiation():
    from vnstock.api.quote import Quote
    try:
        quote = Quote(source="VCI", symbol="ACB", show_log=False)
        assert quote is not None
        assert quote.source.lower() == "vci"
    except ImportError as e:
        pytest.skip(f"Optional charting dependency missing: {e}")


def test_quote_invalid_source_raises():
    from vnstock.api.quote import Quote
    with pytest.raises((ValueError, Exception)):
        Quote(source="INVALID", symbol="ACB")


def test_kbs_listing_instantiation():
    from vnstock.explorer.kbs.listing import Listing as KBSListing
    listing = KBSListing(show_log=False)
    assert listing is not None


def test_kbs_quote_instantiation():
    from vnstock.explorer.kbs.quote import Quote as KBSQuote
    quote = KBSQuote(symbol="ACB", show_log=False)
    assert quote is not None
