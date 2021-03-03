# coding: utf-8

def main():
	# a = [[1], [2], [3]]
	# b = [[4], [5], [6]]
	# a = b
	# print(a)
	# print(3//2)
	for i in range(10, -1, -1):
		print(i)

def test():
    extensions = {
        [PackNameEnum.Common]: [
            ["BaseItem", BaseItem],
            ["InputTextField", InputTextField],
            ["ModuleTopPanel", ModuleTopPanel],
            ["ProgressBar", ProgressBar],
            ["UIProgressBar", UIProgressBar],
            ["TabButtonItem", TabButtonItem],
            ["TabButtonItem1", TabButtonItem1],
            ["TabButtonItem2", TabButtonItem2],
            ["TabButtonItem3", TabButtonItem3],
            ["TabButtonItem4", TabButtonItem4],
            ["AttrItem1", AttrItem1],
            ["AttrItem2", AttrItem2],
            ["AttrItem3", AttrItem3],
            ["AttrItem4", AttrItem4],
            ["AttrTxtItem", AttrTxtItem],
            ["NumberInput", NumberInput],
            ["NumberInput2", NumberInput2],
            ["PhyleIconList", PhyleIconList],
            ["HeroItem", HeroItem],
            ["HeroItem1", HeroItem1],
            ["HeroItem2", HeroItem2],
            ["HeroContainertem", HeroContainertem],
            ["SkillItem", SkillItem],
            ["CostItem1", CostItem1],
            ["CostItem2", CostItem2],
            ["StarList", StarList],
            ["StarItem", StarItem],
            ["ProgressBarCommon", ProgressBarCommon],
            ["ItemGotoGetCell", ItemGoToGetCell],
            ["PlayerAvatarItem", PlayerAvatarItem],
            ["PlayerAvatarItem2", PlayerAvatarItem2],
            ["TimerButton", TimerButton],
            ["TimerText", TimerText],
            ["EnoughItemUI", EnoughItem],
            ["RewardBoxItemUI", RewardBoxItem],
            ["PlayerMedalItem", PlayerMedalItem],
            ["EquipItem", EquipItem],
            ["MoneyItem", MoneyItem],
            ["MoneyItem2", MoneyItem2],
            ["TitleLabel", TitleLabel],
            ["SkillItem1", SkillItem1],
        ],
        [PackNameEnum.Test]: [
            ["TestParamItem", TestParamItem],
            ["TestOptItem", TestOptItem],
            ["TestMsgLogItem", TestMsgLogItem],
            ["TestBaseItem", TestBaseItem]
        ],
        [PackNameEnum.Navbar]: [
            ["NavbarTopPanel", NavbarTopPanel],
            ["NavbarLifeBar", NavbarLifeBar],
        ],

        [PackNameEnum.Pack]: [
            ["PackDebrisItem", PackDebrisItem],
        ],

        [PackNameEnum.Player]: [
            ["PlayerHeroItem", PlayerHeroItem],
        ],

        [PackNameEnum.Formation]: [
            ["FormationItem", FormationItem],
            ["FormationGrid", FormationGrid],
            ["FormationHeroItem", FormationHeroItem],
            ["FormationArrangeItem", FormationArrangeItem],
            ["FormationRestraintItem", FormationRestraintItem],
            ["FormationCampAttrItem", FormationCampAttrItem],
            ["FormationBuffButton", FormationBuffButton],
            ["FormationIcon", FormationIcon],
        ],

        [PackNameEnum.Hero]: [
            ["HeroEquipItem", HeroEquipItem],
            ["HeroEquipReplaceItem", HeroEquipReplaceItem],
            ["HeroStarItem", HeroStarItem],
            ["HeroAttrItem", HeroAttrItem],
            ["HeroAdditionItem", HeroAdditionItem],
            ["HeroTalentItem", HeroTalentItem],
            ["HeroTalentOpenItem", HeroTalentOpenItem],
            ["HeroTalentUpSkillItem", HeroTalentUpSkillItem],
            ["HeroTalentUpCostItem", HeroTalentUpCostItem],

        ],

        [PackNameEnum.Friend]: [
            ["MyFriendCell", MyFriendCell],
            ["SuggestFriendCell", SuggestFriendCell],
            ["FriendApplyCell", FriendApplyCell],
        ],

        [PackNameEnum.Mail]: [
            ["MailCellUI", MailCell]
        ],

        [PackNameEnum.Forge]: [
            ["ForgeEquipItem", ForgeEquipItem],
            ["ForgeRecordItem", ForgeRecordItem],
            ["ForgeRuneCellUI", ForgeRuneCell],
        ],

        [PackNameEnum.Chat]: [
            ["TabItem", ChatTabCell],
            ["ChatFriendCell", ChatFriendCell],
        ],

        [PackNameEnum.Voyage]: [
            ["VoyageTaskItem", VoyageTaskItem],
            ["VoyageTaskStarList", VoyageTaskStarList],
            ["VoyageGetNeedItem", VoyageGetNeedItem],
        ],

        [PackNameEnum.Trail]: [
            ["TrailSkillSelectItem", TrailSkillSelectItem],
            ["TrailRankRoleItem", TrailRankRoleItem],
            ["TrailRankRewardItem", TrailRankRewardItem],
            ["TrailRewardItem", TrailRewardItem],
            ["TrailSupportMyItem", TrailSupportMyItem],
            ["TrailSupportFriendItem", TrailSupportFriendItem],

        ],

        [PackNameEnum.PlayerZone]: [
            ["PlayerZoneAvatarItem", PlayerZoneAvatarItem],
            ["PlayerZoneAvatarBoxItem", PlayerZoneAvatarBoxItem],
            ["PlayerZoneBgItem", PlayerZoneBgItem],
            ["PlayerZoneTitleItem", PlayerZoneTitleItem],
            ["PlayerZoneMedalTypeItem", PlayerZoneMedalTypeItem],
            ["PlayerZoneMedalItem", PlayerZoneMedalItem],
            ["PlayerZoneMedalPanel", PlayerZoneMedalPanel],
            ["PlayerZoneSkinItem", PlayerZoneSkinItem],
            ["PlayerZoneMedalIndexItem", PlayerZoneMedalIndexItem],
            ["PlayerZoneMedalShowItem", PlayerZoneMedalShowItem],
        ],

        [PackNameEnum.Arena]: [
            ["ArenaPlayerItem", ArenaPlayerItem],
            ["ArenaIndexRankRewardItem", ArenaIndexRankRewardItem],
            ["ArenaIndexCountRewardItem", ArenaIndexCountRewardItem],
            ["ArenaRankRewardItem", ArenaRankRewardItem],
            ["ArenaRankRoleItem", ArenaRankRoleItem],
            ["ArenaRecordItem", ArenaRecordItem],
            ["ArenaProgressBar", ArenaProgressBar],
            ["ArenaCopyPlayerItem", ArenaCopyPlayerItem],
            ["ArenaResultPlayerItem", ArenaResultPlayerItem],
        ],

        [PackNameEnum.Guild]: [
            ["GuildOpenViewItem", GuildOpenViewItem],
        ],

        [PackNameEnum.Temple]: [
            ["TempleOccupantItem", TempleOccupantItem],
            ["TempleRecordItem", TempleRecordItem],
        ],

        [PackNameEnum.GuildCopy]: [
            ["GuildCopyReworldCell", GuildCopyReworldCell],
            ["GuildCopyRankRewardItem", GuildCopyRankRewardItem],
            ["GuildCopyRankReworldCell", GuildCopyRankReworldCell],
            ["GuildCopyRankCell", GuildCopyRankCell],
            ["GuildCopyLevelCell", GuildCopyLevelCell],
        ],

        [PackNameEnum.GuildSkill]: [
            ["GuildSkillAttrItem", GuildSkillAttrItem],
            ["GuildSkillButton", GuildSkillButton],
            ["GuildSkillItem", GuildSkillItem],
            ["GuildSkillTypeItem", GuildSkillTypeItem],
        ],

        [PackNameEnum.AllianceParty]: [
            ["AlliancePartyHolderItem", AlliancePartyHolderItem],
            ["AlliancePartyRankItem", AlliancePartyRankItem],
        ],
        [PackNameEnum.Thunder]: [
            ["ThunderMapPanel", ThunderMapPanel],
            ["ThunderMapRowItem", ThunderMapRowItem],
            ["ThunderEventItem", ThunderEventItem],
            ["ThunderHireHeroItem", ThunderHireHeroItem],
            ["ThunderFormationGrid", ThunderFormationGrid],
            ["ThunderSkillSelectItem", ThunderSkillSelectItem],
            ["ThunderSkillItem", ThunderSkillItem],
        ],
        [PackNameEnum.DailyTasks]: [
            ["DailyTasksReworldCell", DailyTasksReworldCell],
            ["DailyExperienceTypeButton", DailyExperienceTypeButton],
            ["DailyTasksShareCell", DailyTasksShareCell],
        ],
        [PackNameEnum.Evocation]: [
            ["EvocationHeroItem", EvocationHeroItem],
            ["EvocationHeroRateItem", EvocationHeroRateItem],
            ["HeroShowItem", HeroShowItem],
        ],
        [PackNameEnum.HeroPalace]: [
            ["FsionHeroItem", FsionHeroItem],
            ["FsionHeroSmallItem", FsionHeroSmallItem],
            ["ExchangeItem", ExchangeItem],
            ["StarHeroItem", StarHeroItem],
        ],
        [PackNameEnum.Champion]: [
            ["ChampionTopPlayerItem", ChampionTopPlayerItem],
            ["ChampionPlayerItem", ChampionPlayerItem],
            ["ChampionVSLeftItem", ChampionVSItem],
            ["ChampionVSRightItem", ChampionVSItem],
            ["Champion32Panel", Champion32Panel],
            ["Champion4Panel", Champion4Panel],
            ["ChampionPlayerNameItem", ChampionPlayerNameItem],
            ["ChampionRewardItem", ChampionRewardItem],
            ["ChampionRoundItem", ChampionRoundItem],
            ["ChampionRankRoleItem", ChampionRankRoleItem],
        ],

        [PackNameEnum.ProphetPalace]: [
            ["ProphetNewHeroItem", ProphetNewHeroItem],
            ["ProphetTypeItem", ProphetTypeItem],
            ["ProphetcostCell", ProphetcostCell],
            ["EvocationTipCell", EvocationTipCell],
            ["ProphetRewardCell", ProphetRewardCell],
        ],
        [PackNameEnum.FightTest]: [
            ["FightTestFormationItem", FightTestFormationItem],
        ],
        [PackNameEnum.Stele]: [
            ["SteleHeroItem", SteleHeroItem],
            ["SteleSlotItem", SteleSlotItem],
            ["SteleAttrItem", SteleAttrItem],
            ["StelePotentialItem", StelePotentialItem],
            ["SteleTalentItem", SteleTalentItem],
        ],
        [PackNameEnum.Robot]: [
            ["RobotItem", RobotItem],
            ["RobotSkillDropItem", RobotSkillDropItem],
        ],

        [PackNameEnum.FightResult]: [
            ["FightResultChampionPlayerItem", FightResultChampionPlayerItem]
        ],

        [PackNameEnum.ShopMarket]:
        [
            ["ShopMarketTabCell",ShopMarketTabCell],
            ["ShopMarketCell",ShopMarketCell],
            ["ShopMarkTypeCell",ShopMarkTypeCell],
            ["ShopMarketRandomCell",ShopMarketRandomCell],
        ],
        [PackNameEnum.Welfare]: [
            ["WelfareMonthCardItem", WelfareMonthCardItem],
            ["GrowthFundItem",GrowthFundItem],
        ],
        [PackNameEnum.Rank]:[
            ["FightNumItem",FightNumItem],
            ["ArenaRankItem",ArenaRankItem],
            ["CheckPointItem",CheckPointItem],
            ["CrossShiliantaItem",CrossShiliantaItem],
            ["GuildRankItem",GuildRankItem],
            ["RankTypeItem",RankTypeItem],
        ],

        [PackNameEnum.GuildWar]: [
            ["GuildWarRankItem", GuildWarRankItem],
            ["GuildWarStrongholdItem", GuildWarStrongholdItem],
            ["GuildWarVsItem", GuildWarVsItem],
            ["GuildWarEnemyItem", GuildWarEnemyItem],
            ["GuildWarLogItem", GuildWarLogItem],
            ["GuildWarRewardItem", GuildWarRewardItem],
            ["GuildWarBoxItem", GuildWarBoxItem],
            ["GuildWarRankPlayerItem", GuildWarRankPlayerItem],
            ["GuildWarBuffAttrItem", GuildWarBuffAttrItem],
            ["GuildWarChallengeItem", GuildWarChallengeItem],
            ["GuildWarDefanseLogItem", GuildWarDefanseLogItem]
            
        ],

        [PackNameEnum.SuperFund]:[
            ["SuperFundBtnItem",SuperFundBtnItem],
            ["SuperFundRewardItem",SuperFundRewardItem],
        ]

    }

    print(extensions)

if __name__ == '__main__':
	# main()
    # test()
    print(1111)