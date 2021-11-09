const ethgreen = require('../../util/ethgreen');

describe('ethgreen', () => {
  it('converts number mojo to ethgreen', () => {
    const result = ethgreen.mojo_to_ethgreen(1000000);

    expect(result).toBe(0.000001);
  });
  it('converts string mojo to ethgreen', () => {
    const result = ethgreen.mojo_to_ethgreen('1000000');

    expect(result).toBe(0.000001);
  });
  it('converts number mojo to ethgreen string', () => {
    const result = ethgreen.mojo_to_ethgreen_string(1000000);

    expect(result).toBe('0.000001');
  });
  it('converts string mojo to ethgreen string', () => {
    const result = ethgreen.mojo_to_ethgreen_string('1000000');

    expect(result).toBe('0.000001');
  });
  it('converts number ethgreen to mojo', () => {
    const result = ethgreen.ethgreen_to_mojo(0.000001);

    expect(result).toBe(1000000);
  });
  it('converts string ethgreen to mojo', () => {
    const result = ethgreen.ethgreen_to_mojo('0.000001');

    expect(result).toBe(1000000);
  });
  it('converts number mojo to colouredcoin', () => {
    const result = ethgreen.mojo_to_colouredcoin(1000000);

    expect(result).toBe(1000);
  });
  it('converts string mojo to colouredcoin', () => {
    const result = ethgreen.mojo_to_colouredcoin('1000000');

    expect(result).toBe(1000);
  });
  it('converts number mojo to colouredcoin string', () => {
    const result = ethgreen.mojo_to_colouredcoin_string(1000000);

    expect(result).toBe('1,000');
  });
  it('converts string mojo to colouredcoin string', () => {
    const result = ethgreen.mojo_to_colouredcoin_string('1000000');

    expect(result).toBe('1,000');
  });
  it('converts number colouredcoin to mojo', () => {
    const result = ethgreen.colouredcoin_to_mojo(1000);

    expect(result).toBe(1000000);
  });
  it('converts string colouredcoin to mojo', () => {
    const result = ethgreen.colouredcoin_to_mojo('1000');

    expect(result).toBe(1000000);
  });
});
