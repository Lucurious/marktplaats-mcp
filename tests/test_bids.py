from marktplaats_mcp.server import (
    _extract_highest_bid,
    _format_listing,
    _format_listing_compact,
)


def test_extract_highest_bid_from_cents_and_nested_payload():
    assert _extract_highest_bid({"auction": {"highestBidCents": 14500}}) == 14500


def test_extract_highest_bid_from_euro_text():
    assert _extract_highest_bid("Hoogste bod € 1.250,50") == 125050


def test_format_listing_exposes_bid_fields():
    listing = {
        "itemId": "m123",
        "title": "Test",
        "description": "",
        "priceInfo": {"priceType": "BID", "priceCents": 0},
        "highestBidCents": 14500,
        "location": {},
        "sellerInformation": {},
    }
    result = _format_listing(listing)
    assert result["highest_bid"] == "€ 145.00"
    assert result["highest_bid_cents"] == 14500


def test_compact_listing_exposes_numeric_bid():
    listing = {
        "itemId": "m123",
        "title": "Test",
        "description": "",
        "priceInfo": {"priceType": "BID", "priceCents": 0},
        "currentBidCents": 14500,
        "location": {},
        "sellerInformation": {},
    }
    result = _format_listing_compact(listing)
    assert result["highest_bid"] == 145
    assert result["highest_bid_cents"] == 14500
