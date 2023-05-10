import bot
import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pos', type=str, help='Example Positional Argument')  # will be accesible under args.POS
    args = parser.parse_args()
    bot.run_discord_bot(args.pos)
